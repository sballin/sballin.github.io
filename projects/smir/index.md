<!-- {"full_title": "Spacecraft inspection robot"} -->

# Spacecraft inspection robot

As we contemplate long-term manned missions to Mars and beyond, we need a convenient way to inspect and repair the damage to spacecraft caused by micrometeorites, space debris, and radiation. I designed a robot for this purpose with a team of fellow students in the excellent Human Spaceflight class taught by former astronaut Mike Massimino. The robot is designed to be a companion for spacecraft and space habitats like the International Space Station, and can be deployed to inspect the exterior of any structure in microgravity.

<center><img src="{{top-path}}/{{article-path}}/screen-1.png"/></center>

The robot is cube-shaped with thrusters at the center of each face and an omnidirectional antenna. It also has a camera at the center of each face, and their video feeds are stitched together to form an immersive view of every direction surrounding the robot. Piloting the robot is supposed to be very easy to learn, and would consist of setting a direction in the immersive view and pressing go/reverse at different speeds. Finally, one face also has precision and infrared cameras, a trace gas analyzer, and a flashlight, to closely inspect damaged areas. When the robot is not being used, it can rest and recharge in the airlock.

I created a [simulation]({{top-path}}/{{article-path}}/simulation) of the robot in the ISS environment to train prospective pilots. Interestingly, it runs pretty well on iPhones (20 MB download), but collision detection is slow even on desktops.

<!--  -->

<center><img src="{{top-path}}/{{article-path}}/screen-2.png"/></center>

You can look around the satellite by clicking and dragging, zoom in/out by scrolling, and actuate thrusters with the buttons on the right panel. Your thrusters will fire in the direction you're looking. You do have a limited amount of propellant, which is accurate for this design's proportions. It may seem to run out quickly, but operating the robot in real life would be slow and delicate work.

<center><img src="{{top-path}}/{{article-path}}/screen-3.png"/></center>

The objective is to navigate from the airlock (blue ring) to a halt right above a damaged solar panel (red sphere), without any collisions.

To make this simulation, I used Three.js and an ISS model from [thingiverse](https://www.thingiverse.com/thing:17114). I went a little overboard with the galactic background and lens flares coming from the sun. Conveniently enough, Three.js was happy to use exact distances in meters for the radius of the Earth and the height and size of the ISS. Isn't it cool how you can zoom out and the ISS becomes a tiny speck, but the Earth looks exactly the same? It's because the Earth is freaking huge. Perspective in space must take a lot of getting used to!

I tried to make collision detection faster using octrees, but didn't see a big improvement. Instead of checking for collisions between all faces of the ISS model, for example, octrees divide space into cubes and only check for collisions with the ISS faces that are inside the cube you're situated in.
