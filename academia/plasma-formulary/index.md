<!-- {"full_title": "Plasma formulary"} -->

# Plasma physics formulary

Table of contents:

[TOC]

## Plasma parameters

Debye length: $$\lambda_D \equiv \sqrt{\frac{\epsilon_0KT_e}{ne^2}}$$

The number of particles in a sphere with the Debye length as its radius should be $\gg1$ for collective behavior.

Cyclotron frequency: $$\omega_c = \frac{\|q\|B}{m}$$

Plasma frequency: $$\omega_p = \sqrt{\frac{n_0e^2}{\epsilon_0m}}$$

Larmor radius: $$r_L \equiv \frac{v_\perp}{\omega_c} = \frac{mv_\perp}{\|q\|B}$$

## Adiabatic invariants

Constant for slow changes to the system.

First, the magnetic moment: $$\mu = \frac{mv_\perp^2}{2B}$$

Second, the velocity integral along a magnetic field line: $$J = \int_a^b v_\parallel ds$$

Third: $\Phi$, the total magnetic flux enclosed by a drift surface, though drifts are relatively slow so $\Phi$ is not often conserved.

## Guiding center drifts

From Chen p43.

General force (e.g. gravity): $$\mathbf{v}_f = \frac1q\frac{\mathbf{F}\times\mathbf{B}}{B^2}$$

Electric field: $$\mathbf{v}_E = \frac{\mathbf{E}\times\mathbf{B}}{B^2}$$

Grad-B drift ($\pm$ is sign of $q$): $$\mathbf{v}_{\nabla B} = \pm\frac12 v_\perp r_L \frac{\mathbf{B}\times\nabla B}{B^2}$$

Curvature drift: $$\mathbf{v}_R = \frac{mv_\parallel^2}q\frac{\mathbf{R}_c\times\mathbf{B}}{R_c^2B^2}$$

Polarization drift: $$\mathbf{v}_p = \pm \frac{1}{\omega_c B}\frac{d\mathbf{E}}{dt}$$

## Plasma waves

From Chen p144-145.

Index of refraction: $$N = \frac{c}{v} = \frac{ck}{\omega}$$

### Electron waves (electrostatic)

$\mathbf{B}_0 = 0$ or $\mathbf{k}\parallel\mathbf{B}_0$ (plasma oscillations): $$\omega^2=\omega_p^2+\frac32k^2v_{th}^2$$

$\mathbf{k}\perp\mathbf{B}_0$ (upper hybrid oscillations): $$\omega^2=\omega_p^2+\omega_c^2=\omega_h^2$$

### Ion waves (electrostatic)

$\mathbf{B}_0$ or $\mathbf{k}\parallel\mathbf{B}_0$ (acoustic waves): $$\omega^2 = k^2v_s^2 = k^2\frac{\gamma_eKT_e+\gamma_iKT_i}{M}$$

$\mathbf{k}\perp\mathbf{B}_0$ (electrostatic ion cyclotron waves): $$\omega^2 = \Omega_c^2+k^2v_s^2$$

$\mathbf{k}\perp\mathbf{B}_0$ (lower hybrid oscillations): $$\omega^2 = \omega_l^2 = \Omega_c\omega_c$$

### Electron waves (electromagnetic)

$\mathbf{B}_0 = 0$ (light waves): $$\omega^2 = \omega_p^2+k^2c^2$$

$\mathbf{k}\perp\mathbf{B}_0$, $\mathbf{E}_1\parallel\mathbf{B}_0$ (O wave): $$\frac{c^2k^2}{\omega^2} = 1 - \frac{\omega_p^2}{\omega^2}$$

$\mathbf{k}\perp\mathbf{B}_0$, $\mathbf{E}_1\perp\mathbf{B}_0$ (X wave): $$\frac{c^2k^2}{\omega^2} = 1 - \frac{\omega_p^2}{\omega^2}\frac{\omega^2-\omega_p^2}{\omega^2-\omega_h^2}$$

$\mathbf{k}\parallel\mathbf{B}_0$ (R wave, whistler): $$\frac{c^2k^2}{\omega^2} = 1-\frac{\omega_p^2/\omega^2}{1-(\omega_c/\omega)}$$

$\mathbf{k}\parallel\mathbf{B}_0$ (L wave): $$\frac{c^2k^2}{\omega^2} = 1-\frac{\omega_p^2/\omega^2}{1+(\omega_c/\omega)}$$

### Ion waves (electromagnetic)

$\mathbf{B}_0 = 0$: None

$\mathbf{k}\parallel\mathbf{B}_0$ (Alfvén wave): $$\omega^2=k^2v_A^2$$

$\mathbf{k}\perp\mathbf{B}_0$ (magnetosonic wave): $$\frac{\omega^2}{k^2} = c^2\frac{v_s^2+v_A^2}{c^2+v_A^2}$$

## References

- _Introduction to Plasma Physics and Controlled Fusion_, by Francis F. Chen. Great book to get started and use as an overview of phenomena in plasma.
- _Introduction to Plasma Theory_, by Dwight R. Nicholson. Very clear derivations of things that might seem to have mysterious origins in Chen.
- _[NRL Plasma Formulary](http://www.nrl.navy.mil/ppd/content/nrl-plasma-formulary)_, by J.D. Huba. Dense collection of useful formulas.

<style>
.MathJax_Display {
    margin: 0;
}
</style>
