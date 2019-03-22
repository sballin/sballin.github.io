<!-- {"full_title": "Fun derivations"} -->

# Fun derivations and proofs

## The quadratic formula

I couldn't remember having ever derived it. Wikipedia said it was fun, so I tried:

$$\begin{align}
0 &= ax^2+bx+c = x^2+\frac bax+\frac ca\\\\
0 &= (x+x_1)(x+x_2) = x^2+(x_1+x_2)x+x_1x_2
\end{align}$$

$$\frac ba = x_1+x_2\rightarrow x_2 = \frac ba-x_1$$

$$\frac ca = x_1x_2 = x_1\left(\frac ba -x_1\right)\rightarrow 0 = x_1^2-\frac bax_1+\frac ca := (x_1+x_3)^2$$

We get another quadratic equation which we say has a single solution $x_3$ (why not two?).

$$-\frac ba = 2x_3 \rightarrow x_3 = -\frac b{2a}$$

$$\frac ca = x_3^2 = \frac{b^2}{4a^2}\rightarrow \frac{b^2}{4a^2}-\frac ca = \left(x_1-\frac b{2a}\right)^2$$

$$\pm\sqrt{\frac{b^2}{4a^2}-\frac ca} = x_1-\frac b{2a}$$

$$x_{1,2} = -\frac b{2a}\pm\sqrt{\frac{b^2}{4a^2}-\frac ca} = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

