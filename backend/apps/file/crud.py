from sqlalchemy.orm import Session
from sqlalchemy import select
from array import *
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from sqlalchemy import desc
from fastapi.templating import Jinja2Templates
from uuid import uuid4
from fastapi.responses import FileResponse
import os
from datetime import datetime
import time

from . import models, schemas

templates = Jinja2Templates(directory="templates")


def upload_file(db, user_id, file_name, file_type, file_upload_info: schemas.FileUpload):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    stamp = time.strftime("%Y-%m-%d %H:%M:%S", datetime.now().timetuple())

    if file_type == "FILE":
        db_file = models.File(
            user_id=user_id,
            name=file_name,
            type=file_type,
            desc=file_upload_info.desc,
            extra_info=file_upload_info.extra_info,
            attachments=file_upload_info.attachments,
            create_date=stamp,
            file_template_id=file_upload_info.file_template_id
        )
    elif file_type == "ATTACHMENT":
        db_file = models.File(
            user_id=user_id,
            name=file_name,
            type=file_type,
            desc=file_upload_info.desc,
        )

    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    if file_type == "FILE" and file_upload_info.library_id is not None:
        save_library_file_relation(db, db_file.id, file_upload_info.library_id)

    return db_file.id


def save_library_file_relation(db: Session, file_id: int, library_id: int):
    db_file_lib_relation = models.FileLibrary(
        file_id=file_id,
        lib_id=library_id
    )
    db.add(db_file_lib_relation)
    db.commit()
    db.refresh(db_file_lib_relation)


def create_library(db: Session, library: schemas.CreateLibrary, user_id: int):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    stamp = time.strftime("%Y-%m-%d %H:%M:%S", datetime.now().timetuple())

    db_library = models.Library(
        name=library.name,
        user_id=user_id,
        file_template_id=library.file_template_id,
        create_date=stamp
    )
    db.add(db_library)
    db.commit()
    db.refresh(db_library)
    return db_library.id


def edit_file_template(db: Session, file_template: schemas.EditFileTemplate, user_id: int):
    db.query(models.FileTemplate).filter(models.FileTemplate.id == file_template.id).update(
        {models.FileTemplate.attachments: file_template.attachments,
         models.FileTemplate.extra_informations: file_template.extra_info})
    db.commit()


def create_file_template(db: Session, name: str, icon: str, libIcon: str, information: array, attachments: array,
                         user_id: int):
    db_file_template = models.FileTemplate(
        name=name,
        user_id=user_id,
        attachments=attachments,
        extra_informations=information,
        icon=icon,
        lib_icon=libIcon
    )
    db.add(db_file_template)
    db.commit()
    db.refresh(db_file_template)
    return db_file_template.id


def get_file_templates(db: Session, user_id: int):
    file_templates = db.query(models.FileTemplate).filter(models.FileTemplate.user_id == user_id).all()
    return file_templates


def add_file_template_info(db: Session, user_id: int, info: schemas.AddFileTemplateInfo):
    file_template = db.query(models.FileTemplate).filter(models.FileTemplate.id == info.file_template_id
                                                         and models.FileTemplate.user_id == user_id).one()
    if info.is_attachment_type:
        file_template.attachments[info.id] = info.name
        file_template.update({models.FileTemplate.attachments: file_template.attachments})
    else:
        file_template.extra_informations[info.id] = info.name
        file_template.update({models.FileTemplate.extra_informations: file_template.extra_informations})
    db.commit()


def add_attachment(db: Session, file_id, id, attachment_id):
    file = db.query(models.File).filter(models.File.id == file_id).one()
    file.attachments[id] = attachment_id
    db.query(models.File).filter(models.File.id == file_id).update(
        {models.File.attachments: file.attachments})
    db.commit()


def get_file(db: Session, file_id: int, request):
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if not file:
        return f'No File with file id {file_id}!'
    file_path = file.name
    user_id = file.user_id
    desc = file.desc
    extra_info = file.extra_info
    attachments = file.attachments
    library_id = db.query(models.FileLibrary).filter(models.FileLibrary.file_id == file_id).first()
    return {
        "file_path": file_path,
        "desc": desc,
        "extra_info": extra_info,
        "attachments": attachments,
        "user_id": user_id,
        "file_template_id": file.file_template_id,
        'library': library_id if library_id else None,
        'create_date': file.create_date,
        'shared': False
    }


def download_file(file_id: int, db: Session):
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    path = f'{os.getcwd()}/static/{file.name}'
    return FileResponse(path, filename=file.name)


def get_files(db: Session, user_id: int):
    files = db.query(models.File).filter(models.File.user_id == user_id).all()
    for file in files:
        library_id = db.query(models.FileLibrary).filter(models.FileLibrary.file_id == file.id).first()
        file.library_id = library_id.lib_id if library_id else None
    return files


def get_library(db: Session, user_id: int, library_id: int, request):
    library = db.query(models.Library).filter(
        models.Library.id == library_id and models.Library.user_id == user_id).first()
    if not library:
        raise HTTPException(status_code=404, detail="File not found")

    file_template_id = library.file_template_id
    name = library.name
    createDate = library.create_date

    return {
        "name": name,
        "file_template_id": file_template_id,
        "last_modified": createDate,
        'shared': False,
    }


def get_all_libraries(db: Session, user_id: int):
    libraries = db.query(models.Library).filter(models.Library.user_id == user_id).all()
    for library in libraries:
        library.shared = False
    return libraries


def delete_file(file_id: int, user_id: int, db: Session):
    file = db.query(models.File).filter(models.File.id == file_id and models.Library.user_id == user_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    db.delete(file)
    db.commit()
    return {"message": "File deleted successfully."}


def delete_library(library_id: int, user_id: int, db: Session):
    library = db.query(models.Library).filter(
        models.Library.id == library_id and models.Library.user_id == user_id).first()
    if not library:
        raise HTTPException(status_code=404, detail="library not found")
    db.delete(library)
    db.commit()
    return {"message": "library deleted successfully."}


def set_file_templates(db: Session, user_id: int):
    create_file_template(db, 'Music', 'MusicNoteOutlinedIcon', 'LibraryMusicOutlinedIcon',
                         {1: 'Singer', 2: 'Year', 3: 'Genre'}, {1: 'Cover', 2: 'Lyrics'}, user_id)
    create_file_template(db, 'Movie', 'SlideshowOutlinedIcon', 'MovieFilterOutlinedIcon',
                         {1: 'Director', 2: 'Year', 3: 'Genre'}, {1: 'Subtitle', 2: 'Audio'}, user_id)
    create_file_template(db, 'Book', 'MenuBookOutlinedIcon', 'LibraryBooksOutlinedIcon',
                         {1: 'Author', 2: 'Year', 3: 'Genre'}, {1: 'Cover', 2: 'Summary'}, user_id)
    create_file_template(db, 'Software', 'TerminalOutlinedIcon', 'FilterNoneOutlinedIcon',
                         {1: 'Developer', 2: 'Version'}, {1: 'Patch'}, user_id)
    create_file_template(db, 'Picture', 'InsertPhotoOutlinedIcon', 'PermMediaOutlinedIcon',
                         {1: 'Photographer', 2: 'Date', 3: 'Place'}, {}, user_id)
