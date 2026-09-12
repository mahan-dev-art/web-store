from flask_sqlalchemy import SQLAlchemy
import time

SECRET_KEY = "gfdgjsdbjcbsdugcsdbcfalavcdb654354"
SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
db = SQLAlchemy()

def get_current_time():
    return round(time.time())

SITE_NAME = "MTheck"
LOGO_FILE_ADDRESS = "images/logo.png"
ABOUT_PAGE_HTML = """
    <p>
      <strong>درباره MTeck </strong><br /><br />

      <strong>جایی برای انتخاب هوشمندانه در دنیای تکنولوژی</strong><br /><br />

      MTeck  با هدف ایجاد یک تجربه ساده، شفاف و قابل اعتماد در خرید محصولات تکنولوژی و دیجیتال شکل گرفته است. ما باور داریم خرید آنلاین فقط انتخاب یک محصول و پرداخت هزینه آن نیست؛ بلکه مجموعه‌ای از اطلاعات و تجربه‌هاست که باید در نهایت به یک خرید مطمئن و رضایت‌بخش منجر شود.<br /><br />

      به همین دلیل تلاش می‌کنیم MTeck  را به فروشگاهی تبدیل کنیم که در آن بتوانید محصول مورد نیازتان را راحت‌تر پیدا کنید، اطلاعات آن را بررسی کنید و با آگاهی بیشتری تصمیم بگیرید.<br /><br />

      <strong>مأموریت ما</strong><br /><br />

      مأموریت MTeck ، ساده‌تر کردن دسترسی به محصولات تکنولوژی و ایجاد تجربه‌ای بهتر برای خرید آنلاین است. ما تلاش می‌کنیم با ارائه اطلاعات شفاف، طراحی ساده و فرایند خرید روان، مسیر انتخاب محصول را برای کاربران کوتاه‌تر و قابل فهم‌تر کنیم.<br /><br />

      <strong>چرا MTeck ؟</strong><br /><br />

      در MTeck  به جزئیات تجربه خرید اهمیت می‌دهیم. از نحوه نمایش محصولات و قیمت‌ها گرفته تا فرایند ثبت سفارش و پیگیری آن، هدف ما این است که همه‌چیز تا حد ممکن ساده، واضح و قابل استفاده باشد.<br /><br />

      <strong>شفافیت:</strong>
      اطلاعات محصول و قیمت باید برای مشتری قابل فهم و روشن باشد.<br /><br />

      <strong>تجربه کاربری:</strong>
      فروشگاه باید ساده و کاربردی باشد و کاربر را با پیچیدگی‌های غیرضروری سردرگم نکند.<br /><br />

      <strong>انتخاب بهتر:</strong>
      می‌خواهیم به شما کمک کنیم قبل از خرید، محصول مناسب نیازتان را بهتر بشناسید.<br /><br />

      <strong>اعتماد:</strong>
      اعتماد با شعار ساخته نمی‌شود؛ با عملکرد درست و احترام به مشتری شکل می‌گیرد.<br /><br />

      <strong>نگاه ما به آینده</strong><br /><br />

      MTeck  یک مسیر در حال رشد است. هدف ما فقط اضافه کردن محصولات بیشتر نیست؛ بلکه می‌خواهیم به مرور خدمات، امکانات و تجربه کاربری فروشگاه را بهتر کنیم و بستری بسازیم که کاربران بتوانند با اطمینان بیشتری از آن استفاده کنند.<br /><br />

      <strong>MTeck ؛ انتخاب آگاهانه، تجربه بهتر.</strong>
    </p>
    <ul>
        <li><a href="tel:0904233452">0904233452</a></li>
        <li><a href="tel:021554123">021554123</a></li>
        <li>تهران، خیابان ولیعصر، بالاتر از میدان ونک، کوچه نمونه، پلاک ۱۲، واحد ۴</li>
    </ul>
"""

feature1 = "۷ روز ضمانت بازگشت کالا"
feature1_file_address = "theme-images/return.png"
feature2 = " ارسال رایگان"
feature2_file_address = "theme-images/free-shipping.png"
feature3 = " پرداخت امن"
feature3_file_address = "theme-images/secure-payment.png"
feature4 = " ضمانت کالا"
feature4_file_address = "theme-images/warranty.png"

# فایل های درون static/images را هم بررسی کنید

BANER1_FILE_ADDRESS = "images/baner.png"
BANER2_FILE_ADDRESS = "images/baner2.png"
BANER3_FILE_ADDRESS = "images/baner3.png"