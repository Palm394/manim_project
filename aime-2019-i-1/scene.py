from typing_extensions import runtime
from manim import *


class main(Scene):
    def construct(self):
        eq = MathTex('N = ','9',' + ','99',' + ','999',' + ','9999',' + ... + ','99...999')

        self.play(Write(eq))

        brace = Brace(eq[-1],direction=DOWN,buff=0.2)
        p_eq = Text('321 หลัก',font='Kanit').next_to(brace,direction=DOWN,buff=0.1).scale(0.6)
        Group = VGroup().add(brace,p_eq)

        self.play(Write(Group))

        statement2 = Text('จงหาผลรวมในแต่ละหลักของ N',font='Kanit',weight=LIGHT).next_to(p_eq,direction=DOWN+LEFT)
        statement2.scale(0.6)
        self.play(Write(statement2))

        self.play(FadeOut(Group))
        self.play(FadeOut(statement2))

        self.wait(2)

        self.play(Transform(eq,eq.copy().move_to(2.2*UP)))

        row = VGroup().add(MathTex('9','99','999','9999','.','.','.','99...999').shift(3*RIGHT,UP).arrange(DOWN,center=False,aligned_edge=RIGHT))
        row_brace = Brace(row,direction=RIGHT,buff=0.5,fill_opacity=0.5)
        row_brace_text = MathTex('+').next_to(row_brace,direction=RIGHT)
        row_line = Line().next_to(row,direction=DOWN)

        self.play(TransformFromCopy(eq,row))
        self.play(Write(row_brace),Write(row_brace_text),Create(row_line))

        self.play(FadeOut(row),FadeOut(row_brace),FadeOut(row_brace_text),FadeOut(row_line))

        zero = MathTex('0').scale(5).move_to(0.5*DOWN)
        self.play(Write(zero))
        self.play(Flash(zero,flash_radius=1,line_length=0.5))
        self.wait(1)
        self.play(FadeOutAndShift(zero))

        self.play(FadeToColor(eq[1],color=YELLOW))
        self.wait(3)

        eq_temp = MathTex('N = ','(10 - 1)',' + ','99',' + ','999',' + ','9999',' + ... + ','99...999')
        self.play(FadeTransform(eq,eq_temp))
        self.play(FadeToColor(eq_temp[3],color=YELLOW))

        self.wait(1)

        eq_temp_2 = MathTex('N = ','(10 - 1)',' + ','(100 - 1)',' + ','999',' + ','9999',' + ... + ','99...999').scale(0.8)
        self.play(TransformMatchingTex(eq_temp,eq_temp_2))

        eq_temp = MathTex('N = ','(10 - 1)',' + ','(100 - 1)',' + ','(1000 - 1)',' + ','9999',' + ... + ','99...999').scale(0.8)
        self.play(FadeToColor(eq_temp_2[5],color=YELLOW))
        self.play(TransformMatchingTex(eq_temp_2,eq_temp))

        eq_temp_2 = MathTex('N = ','(10 - 1)',' + ','(100 - 1)',' + ','(1000 - 1)',' + ','(10000 - 1)',' + ... + ','99...999').scale(0.8)
        self.play(FadeToColor(eq_temp[7],color=YELLOW))
        self.play(TransformMatchingTex(eq_temp,eq_temp_2))

        eq_temp = MathTex('N = ','(10 - 1)',' + ','(100 - 1)',' + ','(1000 - 1)',' + ','(10000 - 1)',' + ... + ','99...999').scale(0.8)
        self.play(FadeToColor(eq_temp_2[9],color=YELLOW))
        self.play(TransformMatchingTex(eq_temp_2,eq_temp))

        eq_temp_2 = MathTex('N = ','(10 - 1)',' + ','(100 - 1)',' + ','(1000 - 1)',' + ','(10000 - 1)',' + ... + ','(10...000 - 1)').scale(0.8)
        self.play(TransformMatchingTex(eq_temp,eq_temp_2))

        eq_temp = MathTex('N = ','10 + 100 + 1000 + ... + ','100...000',' - ','(1+1+1+...)')
        self.play(TransformMatchingTex(eq_temp_2,eq_temp))

        eq_temp_brace = Brace(eq_temp[2])
        eq_temp_brace_text = Text('322 หลัก',font='Kanit').scale(0.5).next_to(eq_temp_brace,direction=DOWN)
        eq_temp_brace_2 = Brace(eq_temp[-1])
        eq_temp_brace_2_text = Text('321 ตัว',font='Kanit').scale(0.5).next_to(eq_temp_brace_2,direction=DOWN)

        self.play(Write(eq_temp_brace),Write(eq_temp_brace_text))
        self.play(Write(eq_temp_brace_2),Write(eq_temp_brace_2_text))

        self.play(FadeOut(eq_temp_brace),FadeOut(eq_temp_brace_text))
        self.play(FadeOut(eq_temp_brace_2),FadeOut(eq_temp_brace_2_text))

        eq_temp_2 = MathTex('N = ','10 + 100 + 1000 + ... + ','100...000',' - ','321')
        self.play(TransformMatchingTex(eq_temp,eq_temp_2.shift(UP)))

        ans = MathTex('N = ','111..','1110',' - ','321')
        self.play(Write(ans))

        f_ans = MathTex('N =','1...11','0789') 
        eq_temp_brace = Brace(f_ans[1])
        eq_temp_brace_text = Text('322-4 หลัก',font='Kanit').scale(0.5).next_to(f_ans,direction=2*DOWN) 
        self.play(TransformMatchingTex(ans,f_ans))
        self.play(Write(eq_temp_brace),Write(eq_temp_brace_text))

        self.clear()

        f_f_ans = MathTex('Ans = (322 - 4) + 7 + 8 + 9 = ','342').scale(1.5)
        self.play(Write(f_f_ans))
        self.play(Circumscribe(f_f_ans[1])) 
