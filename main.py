from fpdf import FPDF

path = r"C:"


class pdf(FPDF):
    def header(self):
        self.image(name=f"{path}\q3.jpeg",x=0,y=0,w=235,h=300)


    def starter(self):
        self.add_page(orientation='P')
        self.set_font('Times', size=12)

    def Body(self):
        img_up=self.image(name=r"C:\_a123.jpg",x=31,y=26,w=36,h=36)

        yb=95
        for i in about_F:
            about_txt = self.text(x=13, y=yb, txt=i)
            yb = yb+3
        self.set_font('Helvetica','B',15)
        self.set_text_color(0,0,0)
        about_tl=self.text(x=14,y=87,txt="ABOUT ME")

        add_set= self.set_font('Helvetica','B',13)
        add_tl=self.text(x=28,y=150,txt="Adress:")

        add_txt_set=self.set_font('Helvetica',size=12)
        add_txt =self.text(x=28,y=155,txt="Lorem ipsum dolor sit amit")
        add_txt2 = self.text(x=28, y=160, txt="city-country")

        phone_set = self.set_font('Helvetica', 'B', 13)
        phone_tl = self.text(x=28, y=170, txt="Phone:")

        phone_txt_set = self.set_font('Helvetica', size=12)
        phone_txt = self.text(x=28, y=175, txt="Lorem ipsum dolor sit amit")

        email_set = self.set_font('Helvetica', 'B', 13)
        email_tl = self.text(x=28, y=185, txt="Email:")

        email_txt_set = self.set_font('Helvetica', size=12)
        email_txt = self.text(x=28, y=190, txt="Lorem ipsum dolor sit amit")

        web_set = self.set_font('Helvetica', 'B', 13)
        web_tl = self.text(x=28, y=200, txt="Website or Portfolio:")

        web_txt_set = self.set_font('Helvetica', size=12)
        web_txt = self.text(x=28, y=205, txt="Lorem ipsum dolor sit amit")

        name_set = self.set_font('Times', 'B', 33)
        name_tl = self.text(x=89, y=43, txt="Website or Portfolio:")

        job_set = self.set_font('Helvetica', size=15,style='B')
        job_col = self.set_text_color(80,80,80)
        job_txt = self.text(x=92, y=49, txt="Lorem ipsum dolor sit amit")

        obj_set = self.set_font('Helvetica', size=13)
        obj_col = self.set_text_color(80, 80, 80)
        obj_txt = self.text(x=92, y=59, txt="Lorem ipsum dolor sit amit")

        ex_tl_set = self.set_font('Helvetica', 'B', 18)
        obj_col = self.set_text_color(80, 150, 200)
        ex_tl = self.text(x=92, y=87, txt="EXPERIENCE")
        self.set_draw_color(80,150,200)
        self.line(x1=92,x2=240,y1=91,y2=91)
        self.line(x1=92,x2=240,y1=91.5,y2=91.5)



        ex1_set=self.set_draw_color(100,100,100)
        ex1_ln=self.line(x1=115,x2=115,y1=98,y2=125)
        ex1_dc=self.rect(x=112,y=98,w=5,h=5)


        self.set_font('Arial', 'B', 14)
        ex1_fy_ly_set=self.set_text_color(0,0,0)
        ex1_fy=self.text(x=92,y=102,txt="2000")
        ex1_ly = self.text(x=92, y=107, txt="2000")

        ex1_jtl_set=self.set_font('Arial',"B",15)
        ex1_jtl=self.text(x=122,y=100,txt="Worker")

        ex1_jp_set1 = self.set_text_color(100, 100, 100)
        ex1_jp_set2 = self.set_font('Arial',"B",14)
        ex1_jp_txt= self.text(x=122,y=105,txt="human shie4ld")

        ex1_desc_set1 = self.set_text_color(0, 0, 0)
        ex1_desc_set2 = self.set_font('Arial',size=9)
        y2=110
        for i2 in exp_F:
            ex1_desc_txt= self.text(x=122,y=y2,txt=i2)
            y2=y2 +5

        ex2_set=self.set_draw_color(100,100,100)
        ex2_ln=self.line(x1=115,x2=115,y1=125,y2=152)
        ex2_dc=self.rect(x=112,y=125,w=5,h=5)


        self.set_font('Arial', 'B', 14)
        ex2_fy_ly_set=self.set_text_color(0,0,0)
        ex2_fy=self.text(x=92,y=127,txt="2000")
        ex2_ly = self.text(x=92, y=132, txt="2000")

        ex2_jtl_set=self.set_font('Arial',"B",15)
        ex2_jtl=self.text(x=122,y=125,txt="Worker")

        ex2_jp_set1 = self.set_text_color(100, 100, 100)
        ex2_jp_set2 = self.set_font('Arial',"B",14)
        ex2_jp_txt= self.text(x=122,y=130,txt="human shie4ld")

        ex2_desc_set1 = self.set_text_color(0, 0, 0)
        ex2_desc_set2 = self.set_font('Arial',size=9)
        y3=135
        for i3 in exp_F:
            ex1_desc_txt= self.text(x=122,y=y3,txt=i3)
            y3=y3 +5








#splitting text after certain number of characters and then allowing user to input his data
about_input =("")
about_input='\n'.join(about_input[i:i+25] for i in range(0, len(about_input), 25))
about_F= about_input.split("\n")


#splitting text after certain number of characters and then allowing user to input his data
exp_input =("5555555555555555555555555555555555555555555555555555555555555")
exp_input ='\n'.join(exp_input[i:i+42] for i in range(0, len(exp_input), 42))
exp_F= exp_input.split("\n")






x = pdf()
x.starter()
x.Body()

x.output('test.pdf')




if __name__ == '__main__':
    print("")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
