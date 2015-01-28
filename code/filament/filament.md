# Filament Code

Tokamaks have a transformer coil at the center of the torus that induces a current in the plasma.

<center><a href="http://cswim.org/imageslibrary/tokamak_schema.gif/view"><img src="tokamak.gif"/></a></center>

I'm working on a Python program that uses magnetic sensor measurements to reconstruct the plasma current profile on Columbia's High-beta Tokamak. 

It can calculate the magnetic field at any location resulting from current in a circular coil:

$$B = G(r, z, r_{coil}, z_{coil})\cdot I_{coil}$$

where $G$ is a Green's function of their positions in cylindrical coordinates. For each magnetic sensor, we subtract the coil fields from the sensor's readings to get the field of the plasma current alone. Then we do the linear algebra version of $I = G^{-1}B$ to calculate the plasma current over a grid of different positions.

<center><a href="https://github.com/sballin/filament"><img src="https://raw.githubusercontent.com/sballin/filament/master/resources/reconstruction.gif"/></a></center>

The plasma current in the above image is actually wrong, because the code is not completely precise, and the least-squares inversion of the Green's function matrix makes errors even bigger. The image below shows how accurately the code can predict what a given sensor sees in a shot where only the vertical field coil is active.
 
<center><a href="https://raw.githubusercontent.com/sballin/filament/master/resources/montage.jpg"><img width="450px" src="https://raw.githubusercontent.com/sballin/filament/master/resources/PA2_S22P.png"/></a></center>

I'm currently writing code to account for eddy currents in the machine's stainless steel shells, which will help produce an accurate end result. On a flat piece of metal, eddy currents might look like this:

<center><svg width="600" height="240">
  <rect x="185" y="5" width="230" height="230" stroke="blue" fill="#fff"/>
  <circle cx="300" cy="120" r="100" stroke="blue" fill="#fff" stroke-width="1"/>
  <circle cx="300" cy="120" r="85" stroke="blue" fill="#fff" stroke-width="1"/>
  <circle cx="300" cy="120" r="70" stroke="blue" fill="#fff" stroke-width="1"/>
  <circle cx="300" cy="120" r="55" stroke="blue" fill="#fff" stroke-width="1"/>
  <circle cx="300" cy="120" r="40" stroke="blue" fill="#fff" stroke-width="1"/>
  <circle cx="300" cy="120" r="25" stroke="blue" fill="#fff" stroke-width="1"/>
  <circle cx="300" cy="120" r="10" stroke="blue" fill="#fff" stroke-width="1"/>
  <polygon points="295,15 295,25 303,20" stroke="blue" fill="blue"/>
  <polygon points="295,30 295,40 303,35" stroke="blue" fill="blue"/>
  <polygon points="295,45 295,55 303,50" stroke="blue" fill="blue"/>
  <polygon points="295,60 295,70 303,65" stroke="blue" fill="blue"/>
  <polygon points="295,75 295,85 303,80" stroke="blue" fill="blue"/>
  <polygon points="295,90 295,100 303,95" stroke="blue" fill="blue"/>
  <polygon points="295,105 295,115 303,110" stroke="blue" fill="blue"/>
  <polygon points="303,124 303,134 295,128" stroke="blue" fill="blue"/>
  <polygon points="303,140 303,150 295,145" stroke="blue" fill="blue"/>
  <polygon points="303,155 303,165 295,160" stroke="blue" fill="blue"/>
  <polygon points="303,170 303,180 295,175" stroke="blue" fill="blue"/>
  <polygon points="303,185 303,195 295,190" stroke="blue" fill="blue"/>
  <polygon points="303,200 303,210 295,205" stroke="blue" fill="blue"/>
  <polygon points="303,215 303,225 295,220" stroke="blue" fill="blue"/>
</svg></center>

But there are other possible configurations. The only constraint is that when we add up the currents along a slice of the material (e.g. the blue arrows), their sum is zero. To find the different modes, we imagine that the material is made up of filaments that carry current. The eigenvectors of the system of resistances and inductances between the filaments that correspond to the longest L/R times are the significant eigenmodes. Here, the program has found the top 3 eigenmodes for one of the steel shells:

<center><a href="https://raw.githubusercontent.com/sballin/filament/master/resources/eigen_comparison.jpg"><img src="https://raw.githubusercontent.com/sballin/filament/master/resources/eigenmodes.png"/></a></center>

Check out the project page on [Github](https://github.com/sballin/filament).
