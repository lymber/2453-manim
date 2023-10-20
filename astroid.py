from manim import *

class Astroid(ThreeDScene):
    def construct(self):
        
        #Parâmetro da astroide
        a=2

        #Eixos
        axes = ThreeDAxes(
            x_range=[-(a+1),(a+1),a],
            y_range=[-(a+1),(a+1),a],
            z_range=[-1,2*a+1,2*a],
            x_length=6,
            y_length=6,
            z_length=6*11/10,
            axis_config={"include_ticks": True},
        )

        #Astroide

        astro = ImplicitFunction(
            lambda x,y: (x**2)**(1/3)+(y**2)**(1/3)-a**(2/3),x_range=[-a,a,0.01],y_range=[-a,a,0.01],color=YELLOW)
        # deveria preencher a região, mas não
        #.set_fill(GREEN, opacity=0.5)

        #astroid parametrica indo e voltando
        # graph1=axes.plot(lambda x: np.sqrt(a**(2/3)-(x**2)**(1/3))**3,x_range=[-a,a,.01],color=YELLOW)
        # graph2=axes.plot_parametric_curve(
        #     lambda t: np.array([a*(1-t),-np.sqrt(a**(2/3)-((a*(1-t))**2)**(1/3))**3,0]), t_range=[0,2,0.01],color=YELLOW)
        
        self.add(axes)
        self.play(Create(astro))
        #self.play(Create(graph1))
        #self.play(Create(graph2))

        eq=MathTex(r"x^\frac{2}{3}+y^\frac{2}{3}=a^\frac{2}{3}",color=YELLOW).shift(2*UP+3*RIGHT)
        self.play(FadeIn(eq, scale=0.66))
        self.wait()
        self.play(FadeOut(eq, scale=0.66))

        #Do plano para o espaço
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES,frame_center=[1,-1,2])#, zoom=3/4);

        self.wait()

        # O segmento
        t0=a/3
        v1=[a*(1-t0),-np.sqrt(a**(2/3)-((a*(1-t0))**2)**(1/3))**3,0]
        v2=[a*(1-t0),np.sqrt(a**(2/3)-((a*(1-t0))**2)**(1/3))**3,0]
        slice=Line(v1,v2, color=BLUE)
        self.play(Create(slice))

        l=MathTex(r"L(x)=2y(x)",color=BLUE)
        self.add_fixed_in_frame_mobjects(l)
        self.play(FadeIn(l.to_corner(UR), scale=0.66))
        self.play(FadeOut(l.to_corner(UR), scale=0.66))
        
        # O quadrado
        v3=[a*(1-t0),np.sqrt(a**(2/3)-((a*(1-t0))**2)**(1/3))**3,2*np.sqrt(a**(2/3)-((a*(1-t0))**2)**(1/3))**3]
        v4=[a*(1-t0),-np.sqrt(a**(2/3)-((a*(1-t0))**2)**(1/3))**3,2*np.sqrt(a**(2/3)-((a*(1-t0))**2)**(1/3))**3]
        square=Polygon(v1,v2,v3,v4,color=BLUE).set_fill(RED, opacity=0.5)
       
        self.play(Transform(slice,square))

        a=MathTex(r"A(x)=L^2(x)=4y^2(x)",color=RED)
        self.add_fixed_in_frame_mobjects(a)
        self.play(FadeIn(a.to_corner(UR), scale=0.66))
        self.play(FadeOut(a.to_corner(UR), scale=0.66))
        self.wait()
        self.play(FadeOut(square,slice))
        self.wait()

        # Superfícies - para melhorar

        # def astro1(u,v):
        #     x = max(abs(u),abs(v)) * u /(u**(2/3)+v**(2/3)**(3/2))
        #     y = max(abs(u),abs(v)) * v /(u**(2/3)+v**(2/3)**(3/2))
        #     z = 0
        #     return [x,y,z]

        # teste=(astro1(1,1))[0]
        
        # pl= Surface(
        #     lambda u, v: axes.c2p((astro1(u,v))[0],(astro1(u,v))[1],(astro1(u,v))[2]),
        #     #max(abs(u),abs(v)) * u /(u^(2/3)+v^(2/3)^3/2),max(abs(u),abs(v)) * v /(u^(2/3)+v^(2/3)^3/2),0
        #     resolution=(2, 2),
        #     v_range=[0.01, a],
        #     u_range=[0.01, a],
        #     )

        # pl.set_style(fill_opacity=1)
        # pl.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        # self.add(pl)
        # area = axes.get_area(
        #     graph1,
        #     x_range=(-a,a),
        #     color=(GREEN_B, GREEN_D))#,
        #     #opacity=1,)
        # self.play(Create(area))

        #Volume
        self.play(FadeOut(astro))
        self.play(FadeOut(axes))
        v=MathTex(r"V=\int_{-a}^a A(x)\, dx=\int_{-a}^a \Big(\sqrt{a^{2/3}-x^{2/3}}\Big)^3\, dx=\dfrac{128a^3}{105}",color=YELLOW) 
        self.add_fixed_in_frame_mobjects(v)
        self.play(FadeIn(v, scale=0.66))
        self.wait(2)
        self.play(FadeOut(v, scale=0.66))
        self.wait()
       
