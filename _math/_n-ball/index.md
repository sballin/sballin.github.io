# Formulas for N-Balls

## What?

An N-ball is an N-dimensional ball. This was an extra credit assignment to figure out formulas for the volume and surface area of higher-dimensional balls. This might seem pretty abstract, but it has a cool real-world application: optimizing error-correcting codes has to do with finding the densest way to pack spheres in higher dimensions.

<center><img src="4-sphere.png" width="170px"/></center>

__Table of Contents:__

[TOC]

## Volume of a 4-Sphere

To find the area $v(B^2)R^2$ of a disk $x^2 + y^2 \leq R^2$, we integrate the height $y = \sqrt{R^2-x^2}$ along the diameter to find the area of the upper half. This is not trivial, but we'll save our strength for the 4-sphere. The full area of the disk is

$$v(B^2)R^2 = \int_{-R}^R 2\sqrt{R^2-x^2}\,dx = \pi R^2$$

For the volume $v(B^3)R^3$ of a sphere $x^2 + y^2 + z^2 \leq R^2$, we integrate the area $\pi r^2$ of vertical slices along the diameter. The volume of the sphere is

$$v(B^3)R^3 = \int_{-R}^R \pi(R^2 - x^2)\,dx = \left.\pi\left(R^2x - \frac{x^3}{3}\right)\right|_{-R}^R = \frac{4\pi}3 R^3$$

The generalized volume $v(B^4)R^4$ of a 4-sphere $w^2 + x^2 + y^2 + z^2 \leq R^2$ can be obtained by integrating the volume $4\pi R^3/3$ of spheres along the diameter. The generalized volume of the 4-sphere is

$$v(B^4)R^4 = \int_{-R}^R \frac{4\pi}3 (R^2 - x^2)^{3/2}\,dx$$

To solve this integral, we need to use trigonometric substitution. We substitute $x = R\sin u$, where $dx = R\cos u\,du$ and the limits $-R\leq x\leq R$ become $-\pi/2 \leq u \leq \pi/2$, leaving us with

$$\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{4\pi}3 (R^2 - R^2\sin^2 u)^{3/2} R\cos u\,du = \frac{4\pi}3 \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} R^4(1 - \sin^2 u)^{3/2}\cos u\,du = \frac{4\pi}3 R^4 \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos^4 u\,du$$

To simplify $\cos^4 u$, we can use the identities $\cos^2 u = 1/2\cdot(1 + \cos(2u))$ and $\sin^2 u = 1/2\cdot(1 - \cos(2u))$:

$$\begin{align}
\cos^4 u = \cos^2 u(1-\sin^2 u) = \cos^2 u - \cos^2 u \sin^2 u &= \frac 1 2 + \frac 1 2 \cos(2u) - \left[\frac 1 2 \sin(2u)\right]^2\\\\
&= \frac 1 2 + \frac 1 2 \cos(2u) - \frac 1 4 \left[\frac 1 2 - \frac 1 2 \cos(4u)\right]\\\\
&= \frac 3 8 + \frac 1 2 \left[\cos(2u)+\cos(4u)\right]
\end{align}$$

We can then solve the integral

$$\begin{align}
\frac{4\pi}3 R^4 \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac 3 8 + \frac 1 2 \left(\cos(2u)+\cos(4u)\right)\,du &= \frac{4\pi}3 R^4\left[\left. \frac 3 8 u + \frac 1 4 \sin(2u) + \frac 1 8 \sin(4u)\right] \right|_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\\\\
&= \frac{4\pi}3 R^4\left[\frac{3\pi}{8} \right] = \frac 1 2 \pi^2 R^4
\end{align}$$

## Surface Area of a 4-Sphere

To find the circumference $a(S^1)R$ of a circle $x^2 + y^2 = R^2$, or simply $r(\theta) = R$, we use the formula for arc length $L = \int_a^b \sqrt{r^2+(dr/d\theta)^2}\,d\theta$ in polar coordinates:

$$a(S^1)R = \int_0^{2\pi} \sqrt{r^2+\left(\frac{dr}{d\theta}\right)^2}\, d\theta = \int_0^{2\pi} R\, d\theta = 2\pi R$$

We can also see this as the result of taking the differential of the area $\pi r^2$ of a disk, which gives us $2\pi r dr$, corresponding to the area of the thin ring of width $dr$ that we can think of as circumference.

To find the surface area $a(S^2)R^2$ of a sphere $x^2 + y^2 + z^2 = R^2$, we have a function $z(x,y) = \sqrt{R^2-x^2-y^2}$ which describes the top half, and can integrate $dS = \sqrt{1+z_x^2+z_y^2}\,dA$, where

$$z_x = \frac{-x}{\sqrt{R^2-x^2-y^2}} \; , \; z_y = \frac{-y}{\sqrt{R^2-x^2-y^2}} \longrightarrow \sqrt{1+z_x^2+z_y^2} = \sqrt{1+\frac{r^2}{R^2-r^2}} = \frac{R}{\sqrt{R^2-r^2}}$$

over the disk $0\leq r \leq R$, $0\leq\theta\leq 2\pi$ to obtain the surface area of the top half, and by symmetry we can double it to get the area of the entire sphere:

$$a(S^2)R^2 = 2\int_0^{2\pi}\int_0^R \sqrt{1+z_x^2+z_y^2} = 2\int_0^{2\pi}\int_0^R\frac{Rr}{\sqrt{R^2-r^2}}\, dr = \left. -4\pi R\sqrt{R^2-r^2}\right|_0^R = 4\pi R^2$$

As we did before, we can get this from taking the differential of the volume $4\pi r^3/3$ of a sphere, $4\pi r^2dr$, which is the volume of the thin shell of thickness $dr$ that we can reduce to the surface area.

Now, for the generalized surface area $a(S^3)R^3$ of a 4-sphere $w^2 + x^2 + y^2 + z^2 = R^2$, we have a function $w(x,y,z) = \sqrt{R^2-x^2-y^2-z^2}$, the "top" half of the 4-sphere, with

$$w_x = \frac{-x}{\sqrt{R^2-x^2-y^2-z^2}},\;w_y = \frac{-y}{\sqrt{R^2-x^2-y^2-z^2}},\;w_z = \frac{-z}{\sqrt{R^2-x^2-y^2-z^2}}$$

$$dS = \sqrt{1+w_x^2+w_y^2+w_z^2}\,dV = \sqrt{1+\frac{\rho^2}{R^2-\rho^2}}\,dV = \frac{R}{\sqrt{R^2-\rho^2}}\,dV$$

using spherical coordinates. By symmetry, the total $a(S^3)R^3$ will be the double of this integrand over the volume of the ball $x^2+y^2+z^2\leq R^2$, or $0\leq\rho\leq R$, $0\leq\theta\leq 2\pi$, $0\leq\phi\leq\pi$:

$$a(S^3)R^3 = 2 \int_0^{2\pi}\int_0^{\pi}\int_0^R \frac{R}{\sqrt{R^2-\rho^2}}\rho^2\sin\phi\,d\rho\,d\phi\,d\theta = 8\pi \int_0^R \frac{R\rho^2}{\sqrt{R^2-\rho^2}}\,d\rho$$

We then use the trigonometric substitution $\rho = R\sin\omega$ and $d\rho = R\cos\omega\,d\omega$, where $0\leq\phi\leq R$ becomes $0\leq\omega\leq\pi/2$:

$$8\pi \int_0^{\pi/2}\frac{R^3\sin^2\omega}{\sqrt{R^2-R^2\sin^2\omega}}\,R\cos\omega\,d\omega = 8\pi\int_0^{\pi/2}\frac{R^3\sin^2\omega}{R\cos\omega}\,R\cos\omega\,d\omega = 8\pi R^3\int_0^{\pi/2}\sin^2\omega\,d\omega$$

$$ = 8\pi R^3\int_0^{\pi/2} \frac 1 2 - \frac 1 2 \cos(2\omega)\, d\omega = \left.8\pi R^3 \left[\frac x 2 - \frac 1 4 \sin(2\omega)\right]\right|_0^{\pi/2} = 8\pi R^3 \left(\frac{\pi}{4}\right) = 2\pi^2 R^3$$

We could have also arrived at this result by finding the differential of the generalized volume $\pi^2 r^4/2$ of a 4-dim ball, which is $2\pi^2 r^3\,dr$, the generalized volume of thin shells of 4-dim balls.

## Behavior of Results

Let's compute $v(B^5)R^5$:

$$\begin{align}
v(B^5)R^5 &= \int_{-R}^R \frac12 \pi^2 (R^2 - x^2)^2\,dx = \frac12 \pi^2 \int_{-R}^R R^4-2R^2x^2+x^4\,dx\\\\ &= \frac12 \pi^2\,2\left(R^5-\frac23R^5+\frac{R^5}5\right) = \frac12 \pi^2\left(\frac{16}{15}R^5\right) = \frac8{15}\pi^2R^5 \longrightarrow v(B^5) \approx \boxed{5.26}
\end{align}$$

Next, $v(B^6)R^6$:

$$v(B^6)R^6 = \int_{-R}^R \frac8{15} \pi^2(R^2-x^2)^{5/2}\,dx$$

We substitute $x = R\sin \theta$ where $dx = R\cos \theta\, d\theta$ and $-R\leq x\leq R$ becomes $-\pi/2\leq\theta\leq\pi/2$:

$$\int_{-\pi/2}^{\pi/2} \frac8{15} \pi^2(R^2-R^2\sin^2\theta)^{5/2}\,R\cos \theta\,d\theta = \int_{-\pi/2}^{\pi/2} \frac8{15} \pi^2R^6\cos^6\theta\,d\theta$$

To integrate $\cos^6\theta\,d\theta$, we do integration by parts where $u = \cos^5\theta$ and $dv = \cos\theta\,d\theta$, therefore $du = -5\cos^4\theta\sin\theta\,d\theta$ and $v = \sin\theta$:

$$\begin{align}
\int u\,dv = uv-\int v\,du \longrightarrow \int \cos^5\theta\cos\theta\,d\theta &= \cos^5\theta\sin\theta - \int -5\cos^4\theta\sin^2\theta\,d\theta\\\\
&= \cos^5\theta\sin\theta + 5\int (1-\cos^2\theta)\cos^4\theta\,d\theta\\\\
&= \cos^5\theta\sin\theta + 5\int \cos^4\theta\,d\theta - 5\int\cos^6\theta\,d\theta
\end{align}$$

We see that the integral of $\cos^6\theta\,d\theta$ is on both sides of this equation, and we remember the result of the integral of $\cos^4\theta\,d\theta$, so we now have

$$\begin{align}
6\int\cos^6\theta\,d\theta = \cos^5\theta\sin\theta + 5\int \cos^4\theta\,d\theta \longrightarrow \int_{-\pi/2}^{\pi/2}\cos^6\theta\,d\theta &= \frac16  \left[\left.\cos^5\theta\sin\theta\right|_{-\pi/2}^{\pi/2} + 5\left(\frac{3\pi}8\right)\right]\\\\
&= \frac{15\pi}{48} = \frac{5\pi}{16}
\end{align}$$

Putting this back into our original integral, we obtain

$$v(B^6)R^6 = \frac8{15} \pi^2R^6\int_{-\pi/2}^{\pi/2}\cos^6\theta\,d\theta = \frac8{15} \pi^2R^6 \cdot \frac{5\pi}{16} = \frac{\pi^3}6R^6 \longrightarrow v(B^6) \approx \boxed{5.17}$$

We see that $v(B^n)$ starts decreasing after $n=5$. For $a(S^n)$, taking differentials of numerical results, $a(S^4) = 8\pi^2/3 = 26.3$ and $a(S^5) = \pi^3 = 31.0$ (still rising). Using the formula for $a(S^n)$ found in section 4., 

$$a(S^6) = 2\pi/5\cdot a(S^{4}) = 2\pi/5\cdot(8\pi^2/3) = 16\pi^3/15 \approx \boxed{33.1}$$

$$a(S^7) = 2\pi/6\cdot a(S^{5}) = \pi/3\cdot (2\pi/4\cdot a(S^{3})) = \pi/3\cdot (\pi/2\cdot 2\pi^2) = \pi^4/3 \approx \boxed{32.5}$$

$a(S^n)$ starts decreasing after $n = 6$

## Generalizing the Formula

We need to generalize the integral used to calculate $v(B^n)$:

$$v(B^n) = v\left(B^{n-1}\right)\int_{-\pi/2}^{\pi/2}\cos^n\theta\,d\theta$$

For the integral of $\cos^n\theta\,d\theta$, we do integration by parts, where $u = \cos^{n-1}\theta$ and $dv = \cos\theta\,d\theta$, therefore $du = -(n-1)\cos^{n-2}\theta\sin\theta\,d\theta$ and $v = \sin\theta$:

$$\begin{align}
\int\cos^{n-1}\theta\cos\theta\,d\theta &= \cos^{n-1}\theta\sin\theta + (n-1)\int\cos^{n-2}\theta\sin^2\theta\,d\theta\\\\
&= \cos^{n-1}\theta\sin\theta + (n-1)\int\cos^{n-2}\theta\,d\theta - (n-1)\int\cos^n\theta\,d\theta\\\\
\int\cos^n\theta\,d\theta &= \frac1n \left[\cos^{n-1}\theta\sin\theta + (n-1)\int\cos^{n-2}\theta\,d\theta\right]\\\\
\end{align}$$

By substituting the definite integral of $\cos^{n-2}\theta\,d\theta$ with $v\left(B^{n-2}\right)/v\left(B^{n-3}\right)$ from previous integrals of the same type, we obtain

$$v(B^n) = v\left(B^{n-1}\right)\cdot\frac1n\left[\left.\cos^{n-1}\theta\sin\theta\right|_{-\pi/2}^{\pi/2} + (n-1)\frac{v\left(B^{n-2}\right)}{v\left(B^{n-3}\right)}\right] = \frac{(n-1)\cdot v\left(B^{n-1}\right)\cdot v\left(B^{n-2}\right)}{n\cdot v\left(B^{n-3}\right)}$$

In order to find a more succinct formula, we adopt the notation $I_{n}$ for the definite integral of $\cos^{n}\theta\,d\theta$.

$$v(B^n) = v\left(B^{n-1}\right)I_{n}\,, \qquad I_{n} = \frac{n-1}{n}I_{n-2}$$

Repeating this process for $v\left(B^{n-1}\right)$, we obtain

$$v(B^n) = v(B^{1})I_{2}I_{3}\cdots I_{n}$$

Substituting $I_{n} = (n-1)I_{n-2}/n$ and $I_{n-2} = v\left(B^{n-2}\right)/v\left(B^{n-3}\right)$ gives us

$$\begin{align}
v(B^n) &= v(B^{1})\frac{(n-1)(n-2)\cdots3}{n(n-1)(n-2)\cdots 4}I_{2}I_{3}I_{4}I_{5}I_{6}\cdots I_{n-1}I_{n}\\\\
&= \frac{3}{n}v(B^{1})I_{2}I_{3}\frac{v(B^{2})}{v(B^{1})}\cdot\frac{v(B^{3})}{v(B^{2})}\cdot\frac{v(B^{4})}{v(B^{3})}\cdots\frac{v(B^{n-3})}{v(B^{n-4})}\cdot\frac{v(B^{n-2})}{v(B^{n-3})}\\\\
&= \frac{3}{n}\cdot I_{2}\cdot\frac23I_{1}\cdot v\left(B^{n-2}\right) = \frac{3}{n}\cdot\frac{\pi}{2}\cdot\frac{4}{3}v\left(B^{n-2}\right)\\\\
&= \frac{2\pi}{n}\cdot v\left(B^{n-2}\right)
\end{align}$$

Using differentials, we can make a formula for area:

$$a(S^n) = (n+1)\cdot v\left(B^{n+1}\right) = (n+1)\cdot\frac{2\pi}{n+1}\cdot\left(B^{n-1}\right) = 2\pi\cdot v\left(B^{n-1}\right) = \frac{2\pi}{n-1}\cdot a\left(S^{n-2}\right)$$

## The Gamma Function

If we repeat the formula for $v(B^{n})$ for $v(B^{n-2})$, we have

$$\frac{2\pi}{n}\cdot v\left(B^{n-2}\right) = \frac{2\pi}{n}\cdot\frac{2\pi}{n-2}\cdots\frac{2\pi}{4}\cdot v\left(B^{2}\right) = \frac{(2\pi)^{n/2}}{n(n-2)(n-4)\cdots4}\cdot v\left(B^{2}\right)$$

for even $n$, and for odd $n$ we have

$$\frac{2\pi}{n}\cdot v\left(B^{n-2}\right) = \frac{(2\pi)^{n/2}}{n(n-2)(n-4)\cdots3}\cdot v\left(B^{1}\right)$$

Which we see is analogous to the Gamma function

$$\Gamma(z)=\frac{\Gamma(z+n)}{z(z+1)\cdots(z+n-1)}$$

We can put our values for $v(B^n)$ and some given values of the Gamma function for integers and half-integers in a table:

|             $\mathbf{n}$ |        1       |   2   |        3        |     4     |         5        |     6     |          7         |
|-------------------------:|:--------------:|:-----:|:---------------:|:---------:|:----------------:|:---------:|:------------------:|
|        $\mathbf{v(B^n)}$ |       $2$      | $\pi$ |     $4\pi/3$    | $\pi^2/2$ |    $8\pi^2/15$   | $\pi^3/6$ |    $16\pi^3/105$   |
| $\mathbf{\Gamma(n/2+1)}$ | $\sqrt{\pi}/2$ |  $1$  | $3\sqrt{\pi}/4$ | $2$       | $15\sqrt{\pi}/8$ | $6$       | $105\sqrt{\pi}/16$ |

We see that our series will require the reciprocal of $\Gamma(n/2+1)$ and an additional factor of $\pi^{n/2}$, so the final formulation is

$$v(B^n) = \frac{\pi^{n/2}}{\Gamma\left(\frac n2 + 1\right)}$$
