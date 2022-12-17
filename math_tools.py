import time 
from math import exp, log


class Math_tools:
    """Class contenant des fonctions de resolution de methode mathematique."""

    def pause(self, s) -> 1:
        """Joue le rôle de decorateur."""

        return time.sleep(s)

    def method_trapeze(self, f, a, b, n):
        """
        Retourn l'integrale de la fonction par la methode de trapezes par n subdivision.
        Attributs: f = fonction, a, b = interval [a, b], n = nombre d'itteration. 
        """
        self.pause(0.5)
        i, h, som = 0, (b-a)/n, 0
        while i <= n: 
            x0 = a + i*h
            if x0 != a and x0 != b:
                som = som + f(x0).real
            i = i + 1
        integ = (h/2) * (f(a) + 2*(som) + f(b))

        return f"{round(integ.real, 4)}\nTask  integral by {self.method_trapeze.__name__} done successfully✅✅✅\n"


    def methode_rectangle_gauche(self, f, a, b, n):
        """
        Retourn l'integrale de la fonction par la methode des rectangles à gauche par n subdivision.
        Attributs: f = fonction, a, b = interval [a, b], n = nombre d'itteration.
        """
        self.pause(1)
        i, h, som = 0, (b-a)/n, 0
        while i <= n: 
            x0 = a + i*h
            if x0 != a and x0 != b:
                som = som + f(x0).real
            i = i + 1
        integ = (h) * (f(a) + (som) )

        return f"{round(integ.real, 4)}\nTask  integral by {self.methode_rectangle_gauche.__name__} done successfully✅✅✅\n"
        

    def method_rectangle_droite(self, f, a, b, n):
        """
        Retourn l'integrale de la fonction par la methode des rectangles à droite par n subdivision.
        Attributs: f = fonction, a, b = interval [a, b], n = nombre d'itteration.
        """
        self.pause(1)
        i, h, som = 0, (b-a)/n, 0
        while i <= n: 
            x0 = a + i*h

            if x0 != a and x0 != b:
                som = som + f(x0).real 
            i = i + 1

        integ = (h) * (som + f(b))
        ret = round(integ.real, 4)
        return f"{ret}\nTask  integral by {self.method_rectangle_droite.__name__} done successfully✅✅✅\n"


    def method_point_milieu(self, f, a, b, n):
        """
        Retourn l'integrale de la fonction par la methode des points du milieu par n subdivision.
        Attributs: f = fonction, a, b = interval [a, b], n = nombre d'itteration.
        """
        self.pause(1)
        i, h, som = 0, (b-a)/n, 0
        x0 = a + i*h
        while i <= n: 
            x1 = a + i*h
            m = (x0+x1)/2
            som = som + f(m).real 
            x0 = x1
            i = i + 1

        integ = (h) * (som)
        return f"{round(integ.real, 4)}\nTask  integral by {self.method_point_milieu.__name__} done successfully✅✅✅\n"



    def method_simpson(self, f, a, b, n):
        """
        Retourn l'integrale de la fonction par la methode de simpson par n subdivision.
        Attributs: f = fonction, a, b = interval [a, b], n = nombre d'itteration.
        """
        self.pause(1)
        i, h, som_pair, som_impar = 0, (b-a)/n, 0, 0
        
        while i <= n: 
            x0= a + i*h
            if i%2 == 0 and x0 != a and x0 != b:
                som_pair = som_pair + f(x0).real
            elif i%2==1 and  x0 != a and x0 != b:
                som_impar = som_impar+ f(x0) 
            i = i + 1

        integ = (h/3) * (f(a) + 2*(som_pair) + 4*(som_impar) + f(b))
        return f"{round(integ.real, 4)}\nTask  integral by {self.method_simpson.__name__} done successfully✅✅✅\n"

    def dichotomie(self, f, a, b, epsilon):
        """
        Fonction qui permet de determiné la racine de l'équation f(x)=0 par la methode de dichotomie
        Attributs: f = fonction : a, b = interval [a, b] - epsilon = l'erreur
        """
        c = "______________________________DICHOTOMIE_METHOD______________________________________"
        fo = "___________a_________________b______________m=a+b/2_______________f(b)______________f(m)__________________d(erreur)___"
        print(c, "\n\n", fo)
        
        d = 1
        while d > epsilon:
            self.pause(0.05)
            m = (a+b)/2
            d = abs(b-a)
            print("{:15}, {:15}, {:15}, {:25}, {:25}, {:10}\n".format(a, b, m, f(b), f(m), d)) 
            if m == 0:
                return m
            elif f(a) * f(m) > 0:
                a = m
            else:
                b = m
        
        return f"\n\nAlpha appartient à [{round(a, 4)}; {round(b, 4)}], \nL'erreur est : {d}\nTask dichotomie done successfully✅✅✅"

    def newton(self, f, d, x0, eps):
        """
        Fonction qui permet de determiné la racine de l'équation f(x)=0 par la methode de newton
        Attributs: f = fonction - d = derivé de la fonction - x0 = la valeur x0 initial donnée - eps = l'erreur
        """
        self.pause(1)
        xm = x0 - (f(x0)/d(x0))
        delta = abs(xm-x0)
        i = 1
        while  delta > eps:
            x0 = xm
            xm = x0 - ((f(x0))/( d(x0)))
            delta = abs(xm-x0)
            i += 1
        xm = round(xm.real, 4)
        a = "______________NEWTON METHOD______________________"
        
        return f"\n{a}\nAlpha is  = {xm}; \n\nError is {delta} \n\nValue found in {i}e itteration✅✅✅"




#Essaie des differentes fonction.
test = Math_tools()
print("Methode Trapeze            =>",test.method_trapeze(lambda x: x*log(x), 1, 2, 3))
print("Methode rectangle à gauche =>",test.methode_rectangle_gauche(lambda x: x*log(x), 1, 2, 3))
print("Methode rectangle à droite =>",test.method_rectangle_droite(lambda x: x*log(x), 1, 2, 30))
print("Methode point du milieu    =>",test.method_point_milieu(lambda x: x*log(x), 1, 2, 3))
print("Methode simpson            =>",test.method_simpson(lambda x: x*log(x), 1, 2, 3))
print(test.newton(lambda x: exp(x)-x-2, lambda x:  exp(x)-1, 1, 0.016))
print(test.dichotomie(lambda x: exp(x)-x-2, 0, 1.5, 0.016))
print()
