# SE-Lab-1
این پروژه یک سرویس ساده برای مدیریت فایل های کاربران می باشد، به طوری که کاربران میتوانند فایل های خود را به آپلود، ویرایش و دانلود کنند. این پروژه یک وب اپلیکیشن است و شامل دو بخش backend و frontend میباشد که به صورت مشارکتی توسط اعضای تیم پیاده سازی شده اند. در ادامه توضیحاتی در رابطه با نحوه مدیریت نسخه این پروژه قابل مشاهده هستند:
+ مطابق نیازمندی های پروژه، حداقل 20 کامیت معنادار در این پروژه قابل ایجاد شده اند. برای نامگذاری هر کامیت از توافق شروع با فعل امری استفاده شده است.
+ امکان مرج و پوش بر روی برنچ main تنها به کمک pull request  امکان پذیر است. در تصویر زیر قانون تعریف شده برای محافظت از این شاخه را مشاهده می کنید:
  ![image](https://github.com/mtndaghyani/SE-Lab-1/assets/59438691/83884b71-bff0-4d68-b8c6-21d2c2991a7d)
+ این پروژه دارای 3 برنچ اصلی به جز برنچ main میباشد که مربوط به پیاده سازی فیچرهای مختلف اپ هستند. برای نامگذار آنها از توافق author-type-name استفاده شده است.
+ در فایل .gitignore میتوان فایل هایی را مشاهده کرد که نیاز به track کردن آنها وجود ندارد، مانند فایل های config برای ide ها و ... .
  + حداقل 2 کانفلیکت هنگام مرج کردن با برنچ main ایجاد و برطرف شدند. در تصاویر زیر نمونه ای را ملاحظه می کنید:
    ![image](https://github.com/mtndaghyani/SE-Lab-1/assets/59438691/97622dce-b090-4e3c-ae64-96975fd9d1b1)
    ![image](https://github.com/mtndaghyani/SE-Lab-1/assets/63471751/883c901b-093b-4d22-bdf1-1d0ba8be2d40)

    سوال های بخش 2:
    1)	پوشه‌ی .git در یک مخزن Git شامل تمام اطلاعات مربوط به نسخه‌کنترل نگهداری می‌شود. این اطلاعات شامل تاریخچه تغییرات (commit ها)، شاخه‌ها (branches)، تگ‌ها (tags)، تنظیمات مرتبط با نسخه‌کنترل، اطلاعات در مورد کاربران و مشخصات آن‌ها (از جمله نام و ایمیل) و اطلاعات دیگری مرتبط با مخزن نرم‌افزاری است.هنگامی که یک مخزن Git ایجاد می‌شود، پوشه‌ی.git  به صورت خودکار در root مخزن ایجاد می‌شود. این پوشه نباید دستی تغییر داده شود مگر اینکه شما دقیقاً بدانید چه کاری انجام می‌دهید، زیرا هر گونه تغییر در این پوشه ممکن است به طور جدی از کارکرد مخزن Git شما اختلال ایجاد کند.دستوراتی که می‌توانند یک پوشه .git ایجاد کنند، به صورت خودکار در زمان ایجاد یک مخزن Git اجرا می‌شوند. به عبارت دیگر، شما نیازی به دستور خاصی برای ساختن این پوشه ندارید. به طور خودکار توسط Git ایجاد می‌شود و شامل تمام اطلاعات مورد نیاز برای مدیریت نسخه‌ها و تغییرات در مخزن شما است.
2)	در مفهوم نرم‌افزاری، "atomic" به معنای یکپارچه یا اتمیک است. واژه‌ی "atomic" در زبانی نرم‌افزاری به معنای انجام یک عملیات کامل، کوچک، و یکپارچه است که این عملیات به صورت کامل یا همه یا هیچی انجام می‌شود. به عبارت دیگر، اگر یک عملیات atomic باشد، آن عملیات به صورت کامل و یکپارچه انجام می‌شود یا انجام نمی‌شود.
در مفهوم Commit Atomic:
یک "atomic commit" یعنی یک commit که شامل تغییرات مرتبط با یک وظیفه یا قابلیت خاص در یک پروژه است. این commit شامل تمام تغییرات لازم برای اجرای یک ویژگی خاص یا رفع یک مشکل خاص می‌شود. هر commit باید یک تغییر کوچک و مرتبط با یک مسئله خاص را اعمال کند تا بتواند به عنوان یک atomic commit در نظر گرفته شود.
در مفهوم Pull Request Atomic:
یک "atomic pull request" یا "atomic PR" به معنای ارسال یک درخواست pull که فقط یک تغییر مرتبط با یک قابلیت یا مشکل خاص را شامل می‌شود. این به این معناست که درخواست pull شامل یک مجموعه کوچک از تغییرات است که به صورت کامل و کامل‌ترین شکل ممکن رفع یک مشکل یا افزودن یک قابلیت خاص را انجام می‌دهد. این اجازه می‌دهد به افراد دیگر بررسی کامل و مستقل از این درخواست pull را انجام دهند.
استفاده از atomic commits و atomic pull requests در مدیریت نسخه‌ها و همچنین در فرآیند توسعه‌ی نرم‌افزار بهبودهای قابل توجهی به انجام می‌دهد، از جمله کاهش احتمال کنفلیکت‌ها و افزایش قابلیت فهم و بررسی کد است.
3)	دستورهای `fetch`, `pull`, `merge`, `rebase` و `cherry-pick` در Git به کارهای مختلفی برای مدیریت تغییرات در مخزن نسخه‌کنترلی Git اشاره دارند. در ادامه، تفاوت این دستورها را بیان می‌کنم:
 1. `fetch`:
 `git fetch` داده‌ها را از یک مخزن از راه دور به مخزن محلی شما می‌آورد. این دستور تغییرات را دانلود می‌کند اما مخزن محلی را به‌روز نمی‌کند.شما می‌توانید بعد از اجرای `git fetch` تغییرات را در مخزن محلی با `git merge` یا `git rebase` ادغام کنید.
 2. `pull`:
 `git pull` داده‌ها را از یک مخزن از راه دور به مخزن محلی شما می‌آورد و سپس تغییرات را در مخزن محلی ادغام می‌کند. `git pull` در واقع یک ترکیب از `git fetch` و `git merge` است.
 3. `merge`:
 `git merge` از دو شاخه (برنچ) مختلف تغییرات را به‌روز می‌کند. این دستور یک commit جدید ایجاد می‌کند که تغییرات از دو شاخه را ادغام می‌کند.
 4. `rebase`:
`git rebase` نیز از دو شاخه تغییرات را به‌روز می‌کند، اما با یک روش متفاوت. به جای ایجاد یک commit جدید برای ادغام، `git rebase` تاریخچه commit های فعلی را از یک شاخه دیگر می‌گیرد و آن‌ها را در انتهای تاریخچه فعلی اعمال می‌کند.
 5. `cherry-pick`:
`git cherry-pick` یک commit خاص را از یک شاخه به شاخه دیگر منتقل می‌کند. این دستور از commit های موجود در یک شاخه را انتخاب کرده و آن‌ها را در یک شاخه دیگر اعمال می‌کند، به‌طوری‌که انگار که این commit ها از ابتدا در شاخه دیگر انجام شده‌اند. به‌طور خلاصه، `fetch` داده‌ها را از مخزن از راه دور می‌آورد، `pull` داده‌ها را می‌آورد و سپس ادغام می‌کند، `merge` ادغام تغییرات را انجام می‌دهد، `rebase` تغییرات را به‌روز می‌کند و تاریخچه commit ها را مرتب می‌کند، و `cherry-pick` یک commit را به یک شاخه دیگر انتقال می‌دهد. هرکدام از این دستورها ویژگی‌ها و مزایای خاصی دارند و بسته به موقعیت‌های مختلف در مدیریت تغییرات در پروژه‌های Git مورد استفاده قرار می‌گیرند.
4)	دستورهای `reset`, `revert` و `restore` در Git به کارهای مختلفی برای لغو یا بهبود تغییرات در مخزن نسخه‌کنترلی Git اشاره دارند. در ادامه، تفاوت این دستورها را بیان می‌کنم:
 1. `reset`:
`git reset` به کاربر اجازه می‌دهد تا تغییرات را از commit های مخصوصی لغو کند و شاخه (برنچ) را به commit مشخصی ببرد. این دستور تغییرات را از شاخه حذف می‌کند و شاخه را به commit مورد نظر برمی‌گرداند. این عملیات تغییرات را از تاریخچه‌ی commit های Git حذف می‌کند و تاریخچه‌ی commit های قبلی از آن commit در دسترس نخواهند بود.
 2. `revert`:
 `git revert` به کاربر اجازه می‌دهد تا یک یا چند commit خاص را لغو کند. این دستور یک commit جدید ایجاد می‌کند که تغییرات معکوس شده از commit مورد نظر را اعمال می‌کند. عملیات `revert` تغییرات را از تاریخچه‌ی commit های Git حذف نمی‌کند. به جای اینکه commit های قبلی را حذف کند، یک commit جدید با تغییرات معکوس شده ایجاد می‌کند.
 3. `restore`:
 `git restore` به کاربر اجازه می‌دهد تا تغییرات از فایل‌ها یا شاخه‌ها را لغو کند. این دستور تغییرات را از فایل‌ها یا شاخه‌ها حذف می‌کند و آن‌ها را به حالتی که در commit آخرین بار که در مخزن Git ذخیره شده بودند باز می‌گرداند.
`git restore` به جای ایجاد commit جدید یا انجام تغییرات روی commit ها، تغییرات را مستقیماً از فایل‌ها لغو می‌کند. به طور خلاصه:`reset` تغییرات را از commit ها حذف کرده و شاخه را به commit مشخصی برمی‌گرداند.`revert` یک commit جدید ایجاد کرده و تغییرات معکوس شده از commit مورد نظر را در آن اعمال می‌کند. `restore` تغییرات را از فایل‌ها یا شاخه‌ها حذف کرده و به حالت آخرین commit برمی‌گرداند.
5)	در مفهوم Git، هر commit به عنوان یک "snapshot" (نگاهی کلی و کامل) از مخزن نرم‌افزاری در یک لحظه زمانی خاص در نظر گرفته می‌شود. مفهوم snapshot در Git به این معناست که هر commit شامل یک تصویر کامل از وضعیت فعلی فایل‌ها و پوشه‌ها در مخزن نرم‌افزاری است. این تصویر نشان دهنده تمام تغییرات اعمال شده در فایل‌ها نسبت به commit قبلی است.وقتی یک commit در Git ایجاد می‌شود، تمام فایل‌ها و دایرکتوری‌های موجود در مخزن در آن لحظه زمانی به همراه تاریخچه تغییرات در آن فایل‌ها به صورت یک snapshot ذخیره می‌شوند. هر commit به عنوان یک snapshot از وضعیت مخزن در آن لحظه مشخص می‌شود. این امر به Git این امکان را می‌دهد که به راحتی به هر commit برگردد و وضعیت مخزن را به حالتی که در آن commit ذخیره شده برگرداند.
ارتباط با commit: Commit در Git دقیقاً یک snapshot از مخزن نرم‌افزاری در یک لحظه زمانی مشخص را نمایان می‌کند. هر commit شامل متنی است که توضیح می‌دهد که چه تغییراتی اعمال شده است و همچنین مشخصات فایل‌ها و پوشه‌های تغییر یافته در snapshot را نشان می‌دهد. وقتی که شما یک commit می‌سازید، یک snapshot از وضعیت مخزن در آن نقطه زمانی ایجاد می‌شود. این snapshot شامل تمام فایل‌ها و تغییرات اعمال شده در آن‌ها در آن لحظه است. Commit ها به صورت پشته‌ای در Git ذخیره می‌شوند و شما می‌توانید به آخرین commit یا هر commit دیگری در این پشته بازگردید تا وضعیت مخزن را در آن لحظه مشاهده کنید.بنابراین، مفهوم snapshot در Git به کاربردی مشخص در ارتباط با commit ها دارد، زیرا هر commit به عنوان یک snapshot از وضعیت مخزن در یک لحظه زمانی معین در نظر گرفته می‌شود.

