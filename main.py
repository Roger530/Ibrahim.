from flet import *
import sqlite3
import pandas as pd

# إنشاء اتصال بقاعدة البيانات
conn = sqlite3.connect("dato.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stdname TEXT,
    stdmail TEXT,
    stdphone TEXT,
    stdaddress TEXT,
    stmathmatic INTEGER,
    starabic INTEGER,
    stfrance INTEGER,
    stenglish INTEGER,
    stdrawing INTEGER,
    stchemistry INTEGER
)""")
conn.commit()

def main(page: Page):
    page.title = 'Rakwan'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

    # الحصول على عدد الطلاب
    tabe_name = 'student'
    query = f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]

    # دالة لإضافة طالب جديد
    def add(e):
        cursor.execute(
            "INSERT INTO student (stdname,stdmail,stdphone,stdaddress,stmathmatic,starabic,stfrance,stenglish,stdrawing,stchemistry) VALUES(?,?,?,?,?,?,?,?,?,?)",
            (tname.value, tmail.value, tphone.value, taddress.value,
             int(mathmatic.value), int(arabic.value), int(france.value),
             int(english.value), int(draw.value), int(chemistry.value))
        )
        conn.commit()
        page.snack_bar = SnackBar(Text("تم إضافة الطالب بنجاح", color="white"), bgcolor="green")
        page.snack_bar.open = True
        page.update()
        show(None)  # تحديث العرض لإظهار الطالب الجديد

    # دالة حذف الطالب
    def delete_student(student_id):
        cursor.execute("DELETE FROM student WHERE id = ?", (student_id,))
        conn.commit()
        page.snack_bar = SnackBar(Text("تم حذف الطالب", color="white"), bgcolor="red")
        page.snack_bar.open = True
        page.update()
        show(None)

    # دالة عرض الطلاب
    def show(e):
        page.clean()

        # إعادة إضافة عناصر الصفحة الأساسية (البحث، عدد الطلاب، الأزرار، الحقول)
        page.add(
            ResponsiveRow([
                ResponsiveColumn(
                    content=Image(src="home.gif", width=280),
                    col_sm=12
                )
            ], alignment=MainAxisAlignment.CENTER),

            ResponsiveRow([
                ResponsiveColumn(
                    content=search_field,
                    col_sm=12
                )
            ], alignment=MainAxisAlignment.CENTER),

            ResponsiveRow([
                ResponsiveColumn(
                    content=Text("تطبيق الطالب والمعلم في جيبك", size=18, font_family="IBM Plex Sans Arabic", color='black'),
                    col_sm=12
                )
            ], alignment=MainAxisAlignment.CENTER),

            ResponsiveRow([
                ResponsiveColumn(content=Text(" عدد الطلاب المسجلين : ", size=18, font_family="IBM Plex Sans Arabic", color='blue'), col_sm=6),
                ResponsiveColumn(content=Text(str(row_count), size=18, font_family="IBM Plex Sans Arabic", color='black'), col_sm=6),
            ], alignment=MainAxisAlignment.CENTER, rtl=True),

            ResponsiveRow([
                ResponsiveColumn(content=tname, col_sm=12),
                ResponsiveColumn(content=tmail, col_sm=12),
                ResponsiveColumn(content=tphone, col_sm=12),
                ResponsiveColumn(content=taddress, col_sm=12),
            ]),

            ResponsiveRow([
                ResponsiveColumn(content=marktext, col_sm=12)
            ], alignment=MainAxisAlignment.CENTER, rtl=True),

            ResponsiveRow([
                ResponsiveColumn(content=mathmatic, col_sm=4),
                ResponsiveColumn(content=arabic, col_sm=4),
                ResponsiveColumn(content=france, col_sm=4),
            ], alignment=MainAxisAlignment.CENTER, rtl=True),

            ResponsiveRow([
                ResponsiveColumn(content=english, col_sm=4),
                ResponsiveColumn(content=draw, col_sm=4),
                ResponsiveColumn(content=chemistry, col_sm=4),
            ], alignment=MainAxisAlignment.CENTER, rtl=True),

            ResponsiveRow([
                ResponsiveColumn(content=addbuttn, col_sm=4),
                ResponsiveColumn(content=showbuttn, col_sm=4),
                ResponsiveColumn(content=exportbtn, col_sm=4),
            ], alignment=MainAxisAlignment.CENTER, rtl=True),
        )

        cursor.execute("SELECT * FROM student")
        users = cursor.fetchall()

        if users:
            keys = ['id', 'stdname', 'stdmail', 'stdphone', 'stdaddress', 'stmathmatic', 'starabic', 'stfrance', 'stenglish', 'stdrawing', 'stchemistry']
            result = [dict(zip(keys, values)) for values in users]

            for x in result:
                m = x['stmathmatic']
                a = x['starabic']
                f = x['stfrance']
                e = x['stenglish']
                d = x['stdrawing']
                c = x['stchemistry']
                res = m + a + f + e + d + c
                avg = res / 6

                if avg < 50:
                    status = Text(f"😭 راسب - المعدل: {avg:.2f}", size=16, color='red')
                else:
                    status = Text(f"🥰 ناجح - المعدل: {avg:.2f}", size=16, color='green')

                page.add(
                    Card(
                        color='black',
                        content=Container(
                            content=Column([
                                ListTile(
                                    leading=Icon(icons.PERSON),
                                    title=Text('Name : ' + x['stdname'], color='white'),
                                    subtitle=Text('Student Email : ' + x['stdmail'], color='amber')
                                ),
                                ResponsiveRow([
                                    ResponsiveColumn(content=Text('Phone : ' + x['stdphone'], color='green'), col_sm=6),
                                    ResponsiveColumn(content=Text('Address : ' + x['stdaddress'], color='green'), col_sm=6),
                                ], alignment=MainAxisAlignment.CENTER),

                                ResponsiveRow([
                                    ResponsiveColumn(content=Text('رياضيات : ' + str(x['stmathmatic']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('عربي : ' + str(x['starabic']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('فرنسي : ' + str(x['stfrance']), color='blue'), col_sm=4),
                                ], alignment=MainAxisAlignment.END),

                                ResponsiveRow([
                                    ResponsiveColumn(content=Text('انجليزي : ' + str(x['stenglish']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('رسم : ' + str(x['stdrawing']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('كيمياء : ' + str(x['stchemistry']), color='blue'), col_sm=4),
                                ], alignment=MainAxisAlignment.END),

                                ResponsiveRow([
                                    ResponsiveColumn(content=status, col_sm=12)
                                ], alignment=MainAxisAlignment.CENTER),

                                ResponsiveRow([
                                    ResponsiveColumn(
                                        content=ElevatedButton(
                                            "🗑 حذف",
                                            bgcolor='red',
                                            color='white',
                                            on_click=lambda e, sid=x['id']: delete_student(sid)
                                        ),
                                        col_sm=12
                                    )
                                ], alignment=MainAxisAlignment.CENTER)
                            ])
                        )
                    )
                )
        else:
            page.add(Text("لا يوجد طلاب مسجلين", size=16, color="red", text_align="center"))

        page.update()

    # دالة البحث في الطلاب
    def search(value):
        page.clean()

        query = f"""
            SELECT * FROM student 
            WHERE stdname LIKE ? OR stdmail LIKE ?
        """
        keyword = f"%{value}%"
        cursor.execute(query, (keyword, keyword))
        users = cursor.fetchall()

        if users:
            keys = ['id', 'stdname', 'stdmail', 'stdphone', 'stdaddress', 'stmathmatic', 'starabic', 'stfrance', 'stenglish', 'stdrawing', 'stchemistry']
            result = [dict(zip(keys, values)) for values in users]
            # عرض الطلاب بنفس طريقة show مع التعديل لتناسب البحث
            for x in result:
                m = x['stmathmatic']
                a = x['starabic']
                f = x['stfrance']
                e = x['stenglish']
                d = x['stdrawing']
                c = x['stchemistry']
                res = m + a + f + e + d + c
                avg = res / 6

                if avg < 50:
                    status = Text(f"😭 راسب - المعدل: {avg:.2f}", size=16, color='red')
                else:
                    status = Text(f"🥰 ناجح - المعدل: {avg:.2f}", size=16, color='green')

                page.add(
                    Card(
                        color='black',
                        content=Container(
                            content=Column([
                                ListTile(
                                    leading=Icon(icons.PERSON),
                                    title=Text('Name : ' + x['stdname'], color='white'),
                                    subtitle=Text('Student Email : ' + x['stdmail'], color='amber')
                                ),
                                ResponsiveRow([
                                    ResponsiveColumn(content=Text('Phone : ' + x['stdphone'], color='green'), col_sm=6),
                                    ResponsiveColumn(content=Text('Address : ' + x['stdaddress'], color='green'), col_sm=6),
                                ], alignment=MainAxisAlignment.CENTER),

                                ResponsiveRow([
                                    ResponsiveColumn(content=Text('رياضيات : ' + str(x['stmathmatic']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('عربي : ' + str(x['starabic']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('فرنسي : ' + str(x['stfrance']), color='blue'), col_sm=4),
                                ], alignment=MainAxisAlignment.END),

                                ResponsiveRow([
                                    ResponsiveColumn(content=Text('انجليزي : ' + str(x['stenglish']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('رسم : ' + str(x['stdrawing']), color='blue'), col_sm=4),
                                    ResponsiveColumn(content=Text('كيمياء : ' + str(x['stchemistry']), color='blue'), col_sm=4),
                                ], alignment=MainAxisAlignment.END),

                                ResponsiveRow([
                                    ResponsiveColumn(content=status, col_sm=12)
                                ], alignment=MainAxisAlignment.CENTER),

                                ResponsiveRow([
                                    ResponsiveColumn(
                                        content=ElevatedButton(
                                            "🗑 حذف",
                                            bgcolor='red',
                                            color='white',
                                            on_click=lambda e, sid=x['id']: delete_student(sid)
                                        ),
                                        col_sm=12
                                    )
                                ], alignment=MainAxisAlignment.CENTER)
                            ])
                        )
                    )
                )
        else:
            page.add(Text("لم يتم العثور على نتائج.", size=18, color="red", text_align="center"))

        page.update()

    # الحقول
    tname = TextField(label='اسم الطالب', icon=icons.PERSON, rtl=True, height=38, expand=True)
    # الحقول (تكملة)
    tmail = TextField(label='البريد الالكتروني', icon=icons.MAIL, rtl=True, height=38, expand=True)
    tphone = TextField(label='رقم الهاتف', icon=icons.PHONE, rtl=True, height=38, expand=True)
    taddress = TextField(label='العنوان او السكن', icon=icons.LOCATION_CITY, rtl=True, height=38, expand=True)

    # علامات الطالب
    marktext = Text("Marks Student - علامات الطالب", text_align='center', weight='bold', size=18)

    mathmatic = TextField(label='رياضيات', width=110, rtl=True, height=38)
    arabic = TextField(label='عربي', width=110, rtl=True, height=38)
    france = TextField(label='فرنسية', width=110, rtl=True, height=38)
    english = TextField(label='انجليزي', width=110, rtl=True, height=38)
    draw = TextField(label='رسم', width=110, rtl=True, height=38)
    chemistry = TextField(label='كيمياء', width=110, rtl=True, height=38)

    # زر إضافة طالب جديد
    addbuttn = ElevatedButton(
        "اضافة طالب جديد",
        width=170,
        style=ButtonStyle(bgcolor='blue', color='white', padding=15),
        on_click=add
    )

    # زر عرض كل الطلاب
    showbuttn = ElevatedButton(
        "عرض كل الطلاب",
        width=170,
        style=ButtonStyle(bgcolor='blue', color='white', padding=15),
        on_click=show
    )
    
    # حقل البحث
    search_field = TextField(
        label="بحث بالاسم أو البريد الإلكتروني...",
        width=350,
        on_change=lambda e: search(e.control.value),
        suffix_icon=icons.SEARCH,
        rtl=True
    )
    
    # زر تصدير البيانات إلى CSV (اختياري)
    def export_csv(e):
        cursor.execute("SELECT * FROM student")
        users = cursor.fetchall()
        if users:
            keys = ['id', 'stdname', 'stdmail', 'stdphone', 'stdaddress', 'stmathmatic', 'starabic', 'stfrance', 'stenglish', 'stdrawing', 'stchemistry']
            df = pd.DataFrame(users, columns=keys)
            csv_path = "students_export.csv"
            df.to_csv(csv_path, index=False)
            page.snack_bar = SnackBar(Text(f"تم تصدير البيانات إلى {csv_path}", color="white"), bgcolor="green")
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = SnackBar(Text("لا توجد بيانات للتصدير", color="white"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    exportbtn = ElevatedButton(
        "تصدير CSV",
        width=170,
        style=ButtonStyle(bgcolor='green', color='white', padding=15),
        on_click=export_csv
    )

    # عرض أولي للصفحة مع كل العناصر
    show(None)

app(main)
