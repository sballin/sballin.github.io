# The volume and surface area of n-spheres

What follows was an extra credit assignment to figure out formulas for the volume and surface area of higher-dimensional spheres. This might seem pretty abstract, but it has a cool real-world application: optimizing error-correcting codes has to do with finding the densest way to [pack spheres](https://en.wikipedia.org/wiki/Sphere_packing) in higher dimensions.

<center><img src="{{top-path}}/{{article-path}}/4-sphere.png" width="170px"/></center>

## Volume of a 4-sphere

To find the area $v(B^2)R^2$ of a disk $x^2 + y^2 \leq R^2$, we integrate the height $y = \sqrt{R^2-x^2}$ along the diameter to find the area of the upper half. This is not trivial, but we'll save our strength for the 4-sphere. The full area of the disk is

$$v(B^2)R^2 = \int_{-R}^R 2\sqrt{R^2-x^2}\,dx = \pi R^2$$
