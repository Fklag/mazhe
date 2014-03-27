from phystricks import *

def DS2010ExoGraph():
    pspict,fig=MultiplePictures("DS2010ExoGraph",7)

    #ssfig1 = subfigure(" ")
    #pspict1 = pspicture("logarithme")
    #ssfig2 = subfigure("")
    #pspict2 = pspicture("lnvalabsolue")
    #ssfig3 = subfigure(" ")
    #pspict3 = pspicture("lnxplusun")
    #    ssfig4 = subfigure(" ")
    #pspict4 = pspicture("valabsolueln")
    #ssfig5 = subfigure("")
    #pspict5 = pspicture("unplusln")
    #ssfig6 = subfigure(" ")
    #pspict6 = pspicture("sqrtln")
    #    ssfig7 = subfigure(" ")
    #pspict7 = pspicture("lnsqrt")

    r=1
    eps=exp(-2)
    # Fonctions
    x=var('x')
        
    f1=ln(x)
    f2=ln(abs(x))
    f3=ln(x+r)
    f4=ln(x)+r
    f5=abs(ln(x))
    f6=sqrt(ln(x))
    f7=ln(x**2)


        # Graphes
        
    F1=phyFunction(f1).graph(eps,2)
    F2a=phyFunction(f2).graph(eps,2)
    F2b=phyFunction(f2).graph(-2, -eps)
    F3=phyFunction(f3).graph(eps-1,2)
    F4=phyFunction(f4).graph(eps,2)
    F5=phyFunction(f5).graph(eps,3)
    F6=phyFunction(f6).graph(1,3)
    F7a=phyFunction(f7).graph(eps,2)
    F7b=phyFunction(f7).graph(-2, -eps)


        # Figures
        # pspict1.DrawGraph(F0)
    pspict[0].DrawGraph(F1)
    pspict[0].BB.AddX(-0.5)
    pspict[0].BB.AddY(3.5)
    pspict[0].DrawDefaultAxes()
    pspict[0].dilatation(1)

    pspict[1].DrawGraph(F2a)
    pspict[1].DrawGraph(F2b)
    pspict[1].BB.AddX(-2)
    pspict[1].BB.AddY(3)
    pspict[1].DrawDefaultAxes()
    pspict[1].dilatation(1)

    pspict[2].DrawGraph(F3)
    pspict[2].BB.AddX(-2)
    pspict[2].BB.AddY(3)
    pspict[2].DrawDefaultAxes()
    pspict[2].dilatation(1)

    pspict[3].DrawGraph(F4)
    pspict[3].BB.AddX(-1)
    pspict[3].BB.AddY(3)
    pspict[3].DrawDefaultAxes()
    pspict[3].dilatation(1)

    pspict[4].DrawGraph(F5)
    pspict[4].BB.AddX(-2)
    pspict[4].BB.AddY(3)
    pspict[4].BB.AddY(-3)
    pspict[4].DrawDefaultAxes()
    pspict[4].dilatation(1)

    pspict[5].DrawGraph(F6)
    pspict[5].BB.AddX(-2)
    pspict[5].BB.AddY(3)
    pspict[5].BB.AddY(-3)
    pspict[5].DrawDefaultAxes()
    pspict[5].dilatation(1)

    pspict[6].DrawGraph(F7a)
    pspict[6].DrawGraph(F7b)
    pspict[6].BB.AddX(-2)
    pspict[6].BB.AddY(3)
    pspict[6].DrawDefaultAxes()
    pspict[6].dilatation(1)

    
    fig.conclude()
    fig.write_the_file()