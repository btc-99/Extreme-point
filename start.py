from manimlib import *
from os import system
import numpy as np


class MyProject(Scene):

    def construct(self):
        axes = Axes(
            x_range=(-0.5, 4),
            y_range=(-0.5, 4),
            height=6,
            width=8,
            axis_config={
                "include_tip": True
            }
        )
        
        self.wait()
        self.play(Write(axes, lag_ratio=0.1, run_time=1))

        log_graph = axes.get_graph(
            lambda x: x - np.log(x),
            x_range = [0.05, 4, 0.05],
            color=BLUE
        )
        log_label = axes.get_graph_label(log_graph, Tex("f(x)"))
        self.play(ShowCreation(log_graph), FadeIn(log_label, RIGHT))
        fun_graph = VGroup(axes, log_graph, log_label)

        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(1, log_graph))
        self.play(FadeIn(dot, scale=0.5))
        fun_graph.add(dot)

        h_line = axes.get_h_line(dot.get_left())
        v_line = axes.get_v_line(dot.get_bottom())
        self.play(ShowCreation(h_line), ShowCreation(v_line))
        x_0 = Tex('x_0')
        fx0 = Tex('f(x_0)', font_size=40)
        self.play(Write(x_0.move_to(axes.c2p(1, -0.2))), Write(fx0.move_to(axes.c2p(-0.4, 1))))
        fun_graph.add(h_line, v_line, x_0, fx0)

        m = 2
        line_graph = axes.get_graph(
            lambda x: m,
            x_range = [0, 4, 1],
            color=GOLD
        )
        mm = Tex('m', color=GOLD)
        self.play(Write(mm.move_to(axes.c2p(-0.2, 2))), ShowCreation(line_graph))
        fun_graph.add(mm, line_graph)
        
        dot1 = Dot(color=RED_B)
        dot2 = Dot(color=RED_B)
        x1,x2 = 0.158594, 3.14619
        dot1.move_to(axes.i2gp(x1, log_graph))
        dot2.move_to(axes.i2gp(x2, log_graph))
        self.play(Write(dot1), Write(dot2))
        fun_graph.add(dot1, dot2)

        v1_line = axes.get_v_line(dot1.get_bottom())
        v2_line = axes.get_v_line(dot2.get_bottom())
        self.play(ShowCreation(v1_line), ShowCreation(v2_line))
        x_1 = Tex('x_1')
        x_2 = Tex('x_2')
        self.play(
            Write(x_1.move_to(axes.c2p(x1, -0.2))), 
            Write(x_2.move_to(axes.c2p(x2, -0.2)))
        )
        fun_graph.add(v1_line, v2_line, x_1, x_2)

        self.play(
            fun_graph.animate.scale(0.75).to_edge(LEFT),
            run_time=1,
        )

        ch1 = Text('极值点偏移', font="KaiTi").move_to(2 * UP + 3 *RIGHT)
        self.play(FadeIn(ch1))
        en1 = Tex('f\'(x_0) = 0, f(x_1) = f(x_2) = m')
        self.play(Write(en1.next_to(ch1, 3 * DOWN)))
        en2 = Tex('prove: \ x_1 + x_2 > 2x_0')
        self.play(Write(en2.next_to(en1, 2 * DOWN)))
        en3 = Tex('F(x) = f(x) - f(2x_0-x)')
        self.play(Write(en3.next_to(en2, 3 * DOWN)))

        checkmark = Checkmark()
        exmark = Exmark()
        checkmark.set_color(GREEN).next_to(en3, DOWN)
        exmark.set_color(RED).next_to(en3, DOWN)
        self.add(checkmark)

        self.wait()
        en4 = Tex('prove: \ x_1 + x_2 > g(m)').next_to(en1, 2 * DOWN)
        self.play(ReplacementTransform(en2, en4))
        self.play(ReplacementTransform(checkmark, exmark))

        self.wait()
        self.clear()

        eq1 = Tex('f(x)=x^2', font_size=72)
        self.play(Write(eq1))
        self.wait()
        self.play(eq1.animate.shift(3 * UP))

        axes1 = Axes(
            x_range=(-2, 2),
            y_range=(0, 5),
            height=4,
            width=5,
            axis_config={
                "include_tip": True
            }
        )
        self.play(Write(axes1, lag_ratio=0.1, run_time=1))
        para_graph = axes1.get_graph(
            lambda x: x ** 2,
            color=BLUE
        )
        para_label = axes1.get_graph_label(para_graph, Tex("f(x)=x^2"))
        self.play(ShowCreation(para_graph), FadeIn(para_label, RIGHT))
        fun_graph1 = VGroup(axes1, para_graph, para_label)

        self.play(fun_graph1.animate.shift(4 * LEFT))

        eq2 = Tex('x_1^2=x_2^2=m').move_to(1 * UP + 3 *RIGHT)
        self.play(Write(eq2))
        eq3 = Tex('x_1=-\\sqrt{m}, x_2=\\sqrt{m}').next_to(eq2, 2 * DOWN)
        self.play(FadeIn(eq3))
        eq4 = Tex('x_1+x_2=0').next_to(eq3, 2 * DOWN)
        self.play(Write(eq4))
        fun_graph2 = VGroup(eq2, eq3, eq4)
        ch2 = Text('能不能计算出f(x)的反函数x(m)?', font="KaiTi", font_size=25).move_to(UP + 3 *RIGHT)
        self.play(ReplacementTransform(fun_graph2, ch2))
        ch3 = Text('如果能够用m表示x, 那么就变成单变量问题了', font="KaiTi", font_size=20).next_to(ch2, 2 * DOWN)
        self.play(Write(ch3))
        ch4 = Text('然而一般情况下解析解是很难求出的!', font="KaiTi", font_size=20).next_to(ch3, 2 * DOWN)
        self.play(Write(ch4))
        self.wait()
        self.clear()

        ch1 = Text('我们只能退而求其次,期望求出相应的级数解', font="KaiTi", font_size=25)
        self.play(Write(ch1))
        self.wait()
        self.play(ch1.animate.shift(3 * UP))
        ch2 = Text('我们比较熟悉的是泰勒级数：', font="KaiTi", font_size=25).next_to(ch1, 2 * DOWN)
        self.play(Write(ch2))
        eq1 = Tex('f(x)=', '\\sum_{k=0}^n \\frac{1}{k!}f^{(n)}(x_0) (x-x_0)^k', '+', '\\frac{1}{n!} \\int_{x_0}^x (x-t)^n f^{(n+1)}(t) \\mathrm{d}t').next_to(ch2, 2 * DOWN)
        self.play(FadeIn(eq1))
        self.play(Indicate(eq1[1]))
        self.wait(1)
        self.play(Indicate(eq1[3]))
        self.wait(1)
        eq2 = Tex('x = f^{-1}(m)=x_0 +\\left[\\frac{\\mathrm{d}f^{-1}(m)}{\\mathrm{d}m}\\right]_{m=x_0}(m-x_0)+\\cdots').next_to(eq1, 2 * DOWN)
        self.play(Write(eq2))
        self.wait()
        self.clear()

        ch1 = Text('拉格朗日反演级数', font="KaiTi", font_size=30)
        self.play(Write(ch1))
        self.wait()
        self.play(ch1.animate.shift(3 * UP))
        eq1 = Tex('x = a + y\\varphi(x)').move_to(2 * UP)
        self.play(Write(eq1))

        eq2 = Tex(
            '\\frac{\\partial x}{\\partial a}=1+y\\varphi\'(x)\\frac{\\partial x}{\\partial a}', 
            ',', 
            '\\frac{\\partial x}{\\partial y}=\\varphi(x)+y\\varphi\'(x)\\frac{\\partial x}{\\partial y}'
        ).next_to(eq1, DOWN)
        self.wait()
        self.play(Write(eq2))
        eq3 = Tex(
            '(1-y\\varphi\'(x))\\frac{\\partial x}{\\partial a}=1',
            ',',
            '(1-y\\varphi\'(x))\\frac{\\partial x}{\\partial y}=\\varphi(x)'
        ).next_to(eq1, DOWN)
        self.wait()
        self.play(ReplacementTransform(eq2, eq3))
        eq4 = Tex('\\frac{\\partial x}{\\partial y}=\\varphi(x) \\frac{\\partial x}{\\partial a}').next_to(eq1, 2 * RIGHT)
        self.wait()
        self.play(ReplacementTransform(eq3, eq4))
        eq14 = VGroup(eq1, eq4)
        eq4 = Tex('x = a + y\\varphi(x),', '\\frac{\\partial x}{\\partial y}=\\varphi(x) \\frac{\\partial x}{\\partial a}').move_to(2 * UP)
        self.wait()
        self.play(ReplacementTransform(eq14, eq4))

        eq5 = Tex(
            '\\frac{\\partial}{\\partial y}\\left[F(x) \\frac{\\partial x}{\\partial a}\\right]',
            '=',
            '\\frac{\\partial}{\\partial a}\\left[F(x) \\frac{\\partial x}{\\partial y}\\right]'
        ).next_to(eq4, DOWN)
        self.play(Write(eq5))

        eq6 = Tex(
            'If: \ ',
            '\\frac{\\partial^n x}{\\partial y^n}',
            '=',
            '\\frac{\\partial^{n-1}}{\\partial a^{n-1}}\\left[\\varphi^n(x) \\frac{\\partial x}{\\partial a}\\right]'
        ).next_to(eq5, DOWN)
        self.play(Write(eq6))


        eq7 = Tex(
            'Then: \ ',
            '\\frac{\\partial^{n+1} x}{\\partial y^{n+1}}',
            '=',
            '\\frac{\\partial^{n-1}}{\\partial a^{n-1}}\\frac{\\partial}{\\partial y}\\left[\\varphi^n(x) \\frac{\\partial x}{\\partial a}\\right]'
        ).next_to(eq6, DOWN)
        self.play(Write(eq7))

        eq8 = Tex(
            'Then: \ ',
            '\\frac{\\partial^{n+1} x}{\\partial y^{n+1}}',
            '=',
            '\\frac{\\partial^{n-1}}{\\partial a^{n-1}}\\frac{\\partial}{\\partial a}\\left[\\varphi^n(x) \\frac{\\partial x}{\\partial y}\\right]'
        ).next_to(eq6, DOWN)
        self.wait()
        self.play(ReplacementTransform(eq7, eq8))

        eq9 = Tex(
            'Then: \ ',
            '\\frac{\\partial^{n+1} x}{\\partial y^{n+1}}',
            '=',
            '\\frac{\\partial^{n}}{\\partial a^{n}}\\left[\\varphi^n(x) \\frac{\\partial x}{\\partial y}\\right]'
        ).next_to(eq6, DOWN)
        self.wait()
        self.play(ReplacementTransform(eq8, eq9))

        eq10 = Tex(
            'Then: \ ',
            '\\frac{\\partial^{n+1} x}{\\partial y^{n+1}}',
            '=',
            '\\frac{\\partial^{n}}{\\partial a^{n}}\\left[\\varphi^{n+1}(x) \\frac{\\partial x}{\\partial a}\\right]'
        ).next_to(eq6, DOWN)
        self.wait()
        self.play(ReplacementTransform(eq9, eq10))
        self.wait()
        self.clear()

        ch1 = Text('将x在y=0处展开成泰勒级数', font="KaiTi", font_size=30).move_to(3 * UP)
        self.play(Write(ch1))
        x1 = Tex('x').move_to(6 * LEFT + 1.5 * UP)
        equ1 = Tex('=').next_to(x1, RIGHT)
        eq1 = Tex(
            'a + y\\left[\\frac{\\partial x}{\\partial y}\\right]_0',
            '+',
            '\\frac{y^2}{2!}\\left[\\frac{\\partial^2 x}{\\partial y^2}\\right]_0',
            '+',
            '\\frac{y^3}{3!}\\left[\\frac{\\partial^3 x}{\\partial y^3}\\right]_0'
            '+ \cdots'
        ).next_to(equ1, RIGHT)
        self.play(Write(x1))
        self.play(Write(equ1))
        self.play(Write(eq1))

        equ2 = Tex('=').next_to(equ1, 6 * DOWN)
        eq2 = Tex(
            'a + y\\varphi(a)',
            '+',
            '\\frac{y^2}{2!}\\frac{\\mathrm{d}}{\\mathrm{d} a}\\left[\\varphi^2(a)\\right]',
            '+',
            '\\frac{y^3}{3!}\\frac{\\mathrm{d}^2}{\\mathrm{d} a^2}\\left[\\varphi^3(a)\\right]'
            '+ \cdots'
        ).next_to(equ2, RIGHT)

        self.play(Write(equ2))
        self.play(Write(eq2))

        equ3 = Tex('=').next_to(equ2, 6 * DOWN)
        eq3 = Tex(
            'a + \\sum_k^n \\frac{y^k}{k!}\\frac{\\mathrm{d}^{k-1}}{\\mathrm{d} a^{k-1}}\\left[\\varphi^k(a)\\right]',
            '+\\frac{1}{n!} \\int_0^y (y - t)^n \\frac{\\mathrm{d}^{n}}{\\mathrm{d} a^{n}}\\left[\\varphi^{n+1}(x)',
            '\\frac{\\partial x}{\\partial a}\\right]_{y=t} \\mathrm{d}t',
            font_size=42,
        ).next_to(equ3, RIGHT)

        self.play(Write(equ3))
        self.play(Write(eq3))
        self.wait()
        self.clear()

        eq1 = Tex('y = m - f(x_0) = f(x) - f(x_0)').move_to(3 * UP)
        self.play(Write(eq1))
        eq2 = Tex('1 = \\frac{y}{f(x)-f(x_0)}').next_to(eq1, DOWN)
        self.play(Write(eq2))
        eq3 = Tex('x - x_0 = y \\frac{x - x_0}{f(x) - f(x_0)}=y \\varphi(x)').next_to(eq1, DOWN)
        self.play(ReplacementTransform(eq2, eq3))
        eq4 = Tex('\\lim_{a \\to x_0} \\varphi(a) = \\frac{1}{f\'(x_0)} = \\frac{1}{0}').next_to(eq3, DOWN)
        self.play(Write(eq4))

        all = VGroup(eq1, eq3, eq4)
        self.play(
            all.animate.to_edge(LEFT),
            run_time=1
        )

        axes2 = Axes(
            x_range=(-1, 2),
            y_range=(-1, 2),
            height=4,
            width=4,
            axis_config={
                "include_tip": True
            }
        ).next_to(all, 4 * RIGHT)

        para_graph = axes2.get_graph(
            lambda x: x ** 2 + 1,
            x_range=[-1, 1, 0.01],
            color=BLUE
        )

        line_graph = axes2.get_graph(
            lambda x: x,
            color=WHITE
        )

        anti_para_graph1 = axes2.get_graph(
            lambda x: np.sqrt(x-1),
            x_range=[1, 2, 0.01],
            color=RED
        )
        anti_para_graph2 = axes2.get_graph(
            lambda x: - np.sqrt(x-1),
            x_range=[1, 2, 0.01],
            color=RED
        )

        self.play(Write(axes2, lag_ratio=0.1, run_time=1))
        self.play(ShowCreation(para_graph))
        self.play(ShowCreation(line_graph))
        self.play(ShowCreation(anti_para_graph1), ShowCreation(anti_para_graph2))

        eq5 = Tex('m - f(x_0) = a_2 (x - x_0)^2 + a_3 (x - x_0)^3 + \\cdots').move_to(2 * DOWN)
        self.play(Write(eq5))
        self.wait()
        eq6 = Tex('\\sqrt{m - f(x_0)} = \\sqrt{a_2 (x - x_0)^2 + a_3 (x - x_0)^3 + \\cdots}').move_to(2 * DOWN)
        self.play(ReplacementTransform(eq5, eq6))
        self.wait()
        eq7 = Tex('\\sqrt{m - f(x_0)} = \\sqrt{a_2}(x - x_0) (1 + \\frac{a_3}{a_2} (x - x_0) + \\cdots)^{1/2}').move_to(2 * DOWN)
        self.play(ReplacementTransform(eq6, eq7))
        self.wait()
        eq8 = Tex('\\sqrt{m - f(x_0)} = \\sqrt{a_2} (x - x_0) (1 + \\frac{a_3}{2a_2} (x - x_0) + \\cdots)').move_to(2 * DOWN)
        self.play(ReplacementTransform(eq7, eq8))
        self.wait()
        eq9 = Tex('\\sqrt{m - f(x_0)} = b_1 (x - x_0) + b_2 (x - x_0)^2 + b_3 (x - x_0)^3 + \\cdots').move_to(DOWN)
        self.play(ReplacementTransform(eq8, eq9))
        self.wait()
        eq10 = Tex('y = \\sqrt{m - f(x_0)} = \\sqrt{f(x) - f(x_0)}').next_to(eq9, 
        DOWN)
        self.play(Write(eq10))
        self.wait()
        self.clear()

        axes3 = Axes(
            x_range=(0, 4),
            y_range=(0, 4),
            height=6,
            width=8,
            axis_config={
                "include_tip": True
            }
        ).move_to(0.5 * UP)

        self.play(Write(axes3, lag_ratio=0.1, run_time=1))

        fun1_graph = axes3.get_graph(
            lambda x: x + 1/x -2,
            x_range = [0.2, 4, 0.01],
            color=BLUE
        )
        fun1_label = axes3.get_graph_label(fun1_graph, Tex("y = f(x) - f(x_0)"))
        self.play(ShowCreation(fun1_graph), FadeIn(fun1_label, RIGHT))
        self.wait()

        fun2_graph = axes3.get_graph(
            lambda x: np.sqrt(x + 1/x -2),
            x_range = [0.1, 4, 0.01],
            color=RED
        )
        fun2_label = axes3.get_graph_label(fun2_graph, Tex("y = \\sqrt{f(x) - f(x_0)}"))
        self.play(
            ReplacementTransform(fun1_graph, fun2_graph),
            FadeTransform(fun1_label, fun2_label),
        )
        self.wait(2)
        dot = Dot()
        dot.move_to(axes3.c2p(1, 0))
        self.play(CircleIndicate(dot, run_time=4))
        self.wait()
        self.clear()

        title = Tex('Summary:').move_to(3 * UP)
        self.play(Write(title))
        self.wait()
        tex = TexText(
            r"""
            $\begin{aligned}
            &1. \ m = f(x) \ \Rightarrow \ y = \sqrt{m - f(x_0)} = \sqrt{f(x) - f(x_0)} \\
            &2. \ Construct \ x = a + y \varphi(x) = a + y \frac{x - x_0}{\sqrt{f(x) - f(x_0)}} \\
            &3. \ x_1(y) = a + \sum_k^n \frac{y^k}{k!}\frac{\mathrm{d}^{k-1}}{\mathrm{d} a^{k-1}}\left[\varphi^k(a)\right] + \cdots \\
            &4. \ a \to x_0, x_1(m) = x_0 + \sqrt{m - f(x_0)}\varphi(x_0) + \cdots\\
            &5. \ x_2(m) = [x_1(m)]_{\varphi \to -\varphi}
            \end{aligned}$
            """
        ).next_to(title, 2 * DOWN)
        self.play(Write(tex, runtime=5))
        self.wait()
        self.clear()

        title = Tex('Example \ 1:').move_to(3 * UP + 5 * LEFT)
        self.play(Write(title))
        self.wait()
        eq1 = Tex('f(x) = \\frac{x}{\\ln x}(x>1), \ m = f(x_1) = f(x_2), \ prove: x_1 + x_2 > 2m').move_to(2 * UP)
        self.play(Write(eq1))
        self.wait()
        eq2 = Tex('f\'(x) = \\frac{\\ln x - 1}{(\\ln x)^2} = 0 \ \\Rightarrow (x_0, f(x_0)) = (e, e)').move_to(0.5 * UP)
        self.play(Write(eq2))
        self.wait()
        eq3 = Tex('\\varphi(x) = \\frac{x - x_0}{\\sqrt{f(x)-f(x_0)}} = \\frac{x - e}{\\sqrt{x/\\ln x-e}}').move_to(0.5 * UP)
        self.play(ReplacementTransform(eq2, eq3))
        eq4 = TexText(
            r"""
            $\begin{aligned}
            &x_2(m) = e + \sqrt{2e}\sqrt{m - e} + \frac{5}{3}(m - e) + \frac{1}{2}\int_0^y (y - t)^2 \frac{\mathrm{d}^2}{\mathrm{d}a^2}\left[\frac{\varphi^3(x)}{1-y\varphi'(x)}\right]_{y=t} \mathrm{d}t\\
            &x_1(m) = e - \sqrt{2e}\sqrt{m - e} + \frac{5}{3}(m - e) - \frac{1}{2}\int_0^y (y - t)^2 \frac{\mathrm{d}^2}{\mathrm{d}a^2}\left[\frac{\varphi^3(x)}{1+y\varphi'(x)}\right]_{y=t} \mathrm{d}t
            \end{aligned}$
            """,
            font_size=40
        ).next_to(eq3, DOWN)
        self.play(Write(eq4))
        self.wait()

        eq5 = Tex('x_1 + x_2 = 2e + \\frac{10}{3}(m - e) + o(m-e)').next_to(eq3, DOWN)
        self.play(ReplacementTransform(eq4, eq5))

        eq6 = Tex('x_1 + x_2 > 2m \\Leftrightarrow \\frac{10m-4e}{3}>2m \\Leftrightarrow m>e').next_to(eq5, DOWN)
        self.play(Write(eq6))
        self.wait(2)
        self.clear()

        title = Tex('Example \ 2:').move_to(3 * UP + 5 * LEFT)
        self.play(Write(title))
        self.wait()
        eq1 = Tex('f(x) = \\frac{x}{\\ln x}(x>1), \ m = f(x_1) = f(x_2), \ prove: x_1 + x_2 > m(1 + \ln m)', font_size=42).move_to(2 * UP)
        self.play(Write(eq1))
        self.wait()
        eq2 = Tex('\\varphi(x) = \\frac{x - x_0}{\\sqrt{f(x)(1 + \\ln f(x))-f(x_0)(1 + \\ln f(x_0))}}').move_to(0.5 * UP)
        self.play(Write(eq2))
        self.wait()
        eq3 = Tex('x_1 + x_2 \\sim \\frac{10}{9}m(1+\\ln m)-\\frac{2}{9}e > m(1 + \\ln m) \\Leftrightarrow m(1 + \\ln m) > 2e').next_to(eq2, DOWN)
        self.play(Write(eq3))
        self.wait()


if __name__ == "__main__":
    #system("manimgl {} MyProject".format(__file__))
    system("manimgl {} MyProject -w".format(__file__))