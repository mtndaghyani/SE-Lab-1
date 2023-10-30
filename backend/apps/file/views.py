import aiofiles
import os

from fastapi import APIRouter, Depends, HTTPException, UploadFile, Request
from slowapi.util import get_remote_address
from slowapi import Limiter
from fastapi.responses import HTMLResponse
from services.sql_app.database import get_db
from . import schemas, crud, models
from ..account import crud as user_crud

router = APIRouter(
    prefix='/dashboard',
    tags=['dashboard']
)
limiter = Limiter(key_func=get_remote_address)


def validate_user(db, token):
    if not user_crud.is_user(db, token):
        raise HTTPException(status_code=401, detail="for upload video, login first")
    user_id = user_crud.get_token(db, token).user_id
    return user_id


@router.post("/upload")
async def upload_file(request: Request, file: UploadFile, upload_info: schemas.FileUpload, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    path = f'{os.getcwd()}/static/{file.filename}'
    async with aiofiles.open(path, 'wb+') as out_file:
        content = await file.read()
        await out_file.write(content)
    file_id = crud.upload_file(db, user_id, file.filename, "FILE", upload_info)
    return file_id


@router.post("/upload_attachment")
async def upload_attachment(request: Request, file: UploadFile, upload_info: schemas.AttachmentUpload,
                            db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    path = f'{os.getcwd()}/static/{file.filename}'
    async with aiofiles.open(path, 'wb+') as out_file:
        content = await file.read()
        await out_file.write(content)
    attachment_id = crud.upload_file(db, user_id, file.filename, "ATTACHMENT", upload_info)
    crud.add_attachment(db, upload_info.file_id, upload_info.id, attachment_id)
    return attachment_id


@router.get("/file/{file_id}")
def get_file(request: Request, file_id: int, db=Depends(get_db)):
    validate_user(db, request.cookies['session'])
    return crud.get_file(db, file_id, request)


@router.get("/library/{library_id}")
def get_library(request: Request, token: str, library_id: int, db=Depends(get_db)):
    user_id = validate_user(db, token)
    return crud.get_library(db, user_id, library_id)


@router.post("/create/library")
def create_Library(request: Request, library: schemas.CreateLibrary, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    return crud.create_library(db, library, user_id)


@router.post("/edit/file-template")
def create_file_template(request: Request, fileTemplate: schemas.EditFileTemplate, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    return crud.edit_file_template(db, fileTemplate, user_id)


@router.get("/file-templates")
def get_all_file_templates(request: Request, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    return crud.get_file_templates(db, user_id)


@router.put("/append/file-template-info")
def add_file_template_info(request: Request, token: str, body: schemas.AddFileTemplateInfo, db=Depends(get_db)):
    user_id = validate_user(db, token)
    crud.add_file_template_info(db, user_id, body)
    return "HELL YEAH!!!! new attachment type!!!!"


@router.get("/download/{file_id}")
def download_file(request: Request, file_id: int, db=Depends(get_db)):
    validate_user(db, request.cookies['session'])
    return crud.download_file(file_id, db)


@router.get("/all_files")
def gets_all_files(request: Request, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    return crud.get_files(db, user_id)


@router.get("/all_libraries")
def get_all_libraries(request: Request, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    return crud.get_all_libraries(db, user_id)


@router.delete("/delete_file/{file_id}")
def delete_file(request: Request, file_id: int, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    return crud.delete_file(file_id, user_id, db)


@router.delete("/delete_library/{library_id}")
def delete_library(request: Request, library_id: int, db=Depends(get_db)):
    user_id = validate_user(db, request.cookies['session'])
    return crud.delete_library(library_id, user_id, db)