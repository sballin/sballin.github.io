# ρ(t) <a href="https://github.com/sballin/rho_t"><i class="fa fa-github"></i></a>

<center><a href="http://www.columbia.edu/~sbb2151/rho_t/"><img src="https://raw.githubusercontent.com/sballin/rho_t/master/finals.jpg"/></a></center>

The folks at Columbia's Application Development Initiative made a tool called [Density](https://density.adicu.com) which estimates how full different places around Columbia's campus are using WiFi data. Unfortunately it only gives percentages for the moment you check the site. I wanted to see how the data changed over time.

ρ(t) scrapes data from [density.adicu.com](http://density.adicu.com/) every 15 minutes and shows it all using a D3 graph. Here's the [Github page](https://github.com/sballin/rho_t) for the project.

News: they've made an API that lets you get this data for a range of time, so instead of running a scraper 24/7 as in this project, you could make a nice webapp that does everything client-side.
