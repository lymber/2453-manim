from manim import *

class Ex1_11(Scene):
    def construct(self):
        #Eixos
        axes = Axes(
            x_range=[-5.5, 5.5, 1],
            x_length=11,
            y_range=[-3.5, 3.5, 1],
            y_length=7,
            axis_config={
                "color": GREEN,
                "font_size": 24
            },
            x_axis_config={"numbers_to_exclude": np.arange(-4, 6, 2)},
            y_axis_config={"numbers_to_exclude": np.arange(-2, 4, 2)},
            tips=True
        ).add_coordinates()
        y_label = axes.get_y_axis_label("y", edge=UP, direction=RIGHT, buff=0.6)
        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        #Círculo fixo
        fcircle = Circle(radius=1, color=GREEN)
        fcircle.move_to(RIGHT)

        #Agrupando os objetos fixos iniciais: eixos
        fixed = VGroup(axes,x_label,y_label)
        
        # O parâmetro e seu valor inicial 
        r = ValueTracker(2)

        #Círculo que encolhe
        mcircle = Circle(radius=2, color=RED)
        mcircle.add_updater(
            lambda mobject: mobject.become(Circle(radius=r.get_value(), color=RED))
        )

        #Valor do parâmetro na tela
        rNumber = DecimalNumber(
            r.get_value(),
            color=BLUE,
            num_decimal_places=3,
            show_ellipsis=True
        ).shift(4*LEFT+3*UP)
        #Atualização do valor do parâmetro
        rNumber.add_updater(
            lambda mobject: mobject.set_value(r.get_value())
        )
        # "r=" em LaTeX
        rTex = Tex("$r=$").next_to(rNumber, LEFT).set_color(color=BLUE)

        # A expressão final do limite
        limit = Tex("$\\lim\\limits_{r\\to 0^+} L_r\\stackrel{(?)}{=}4$").set_color(color=BLUE).shift(4*LEFT+3*UP)

        # O ponto P_r do problema, seu atualizador indexado no parâmetro e os textos
        Pr = Dot(axes.coords_to_point(0, 2))
        Pr.add_updater(
            lambda mobject: mobject.become(Dot(axes.coords_to_point(0, (r.get_value()))))
        )
        PrText = Tex("$P_r$").next_to(Pr, UP/2+LEFT)
        PrText.add_updater(
            lambda mobject: mobject.next_to(Pr, UP/2+LEFT)
        )

        # Idem para o ponto Q_r
        Qr = Dot(axes.coords_to_point(2, 0))
        Qr.add_updater(
            lambda mobject: mobject.become(Dot(axes.coords_to_point((r.get_value())**2/2, (r.get_value())*np.sqrt(1-(r.get_value())**2/4))))
        )
        QrText = Tex("$Q_r$").next_to(Qr, (UP+RIGHT)/2)
        QrText.add_updater(
            lambda mobject: mobject.next_to(Qr, (UP+RIGHT)/2)
        )

        # Finalmente o ponto L_r
        Lr = Qr.copy()
        Lr.add_updater(
            lambda mobject: mobject.become(Dot(axes.coords_to_point(2*(np.sqrt(1-(r.get_value())**2/4)+1),0)))
        )
        LrText = Tex("$L_r$").next_to(Lr, (DOWN)/2)
        LrText.add_updater(
            lambda mobject: mobject.next_to(Lr, (DOWN)/2)
        )
        LrValue = DecimalNumber(
            2*(np.sqrt(1-(r.get_value())**2/4)+1),
            color=BLUE,
            num_decimal_places=3,
            show_ellipsis=True
        ).shift(4*LEFT+2*UP)
        LrValue.add_updater(
            lambda mobject: mobject.set_value(2*(np.sqrt(1-(r.get_value())**2/4)+1))
        )
        LrValueTex = Tex("$L_r\sim$").next_to(LrValue, LEFT).set_color(color=BLUE)

        # Agrupando os textos para mexer em bloco
        rText = VGroup(rTex,rNumber)
        LrValueText = VGroup(LrValueTex, LrValue)

        # O segmento ligando P_r a Q_r (fizemos até L_r aqui)
        line = Line(Pr,Lr).set_color(YELLOW)
        line.add_updater(
            lambda mobject: mobject.become(Line(Pr, axes.coords_to_point(2*(np.sqrt(1-(r.get_value())**2/4)+1),0)).set_color(YELLOW))
        )

        # A renderização dos objetos:
        self.play(Create(fixed)) # coisas paradas: eixos 
        self.play(Create(fcircle)) # círculo fixo
        self.play(Create(mcircle)) # círculo que encolhe
        self.add(Pr) # desenha o ponto P_r
        self.play(Write(PrText)) # escreve seu nome no lugar
        self.add(Qr) # desenha o ponto Q_r
        self.play(Write(QrText)) # escreve seu nome no lugar
        self.add(Lr) # desenha o ponto L_r
        self.play(Write(LrText)) # escreve seu nome no lugar
        self.play(Write(rText)) # escreve o valor do parâmetro variando
        self.play(Write(LrValueText)) # escreve o valor de L_r variando
        self.add(line) # desenha o segmento
        self.play(r.animate.set_value(0.001), run_time=8) # faz o parâmetro variar e tudo andar junto em 8 segundos
        self.wait(1) # espera 1 segundo
        self.play(FadeOut(rText,LrValueText)) # apaga os valores de r e L_r
        self.play(FadeIn(limit)) # escreve a conjectura sobre o limite
        self.wait(2) # espera 2 segundos 
        # self.play(FadeOut.clean_up_from_scene()) # um fade no fim da cena
