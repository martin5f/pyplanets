# -*- coding: utf-8 -*-


# PyPlanets: Object-oriented refactoring of PyMeeus, a Python library implementing astronomical algorithms.
# Copyright (C) 2020  Martin Fünffinger
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyplanets.core.base import TOL
from pyplanets.core.constellation import Constellation
from pyplanets.planets.earth import Earth
from pyplanets.planets.saturn import Saturn
from pyplanets.core.epoch import Epoch


# Saturn class

def test_saturn_geometric_heliocentric_position():
    """Tests the geometric_heliocentric_position() method of Saturn class"""

    epoch = Epoch(2018, 10, 27.0)
    lon, lat, r = Saturn(epoch).geometric_heliocentric_position()

    assert abs(round(lon.to_positive(), 4) - 279.5108) < TOL, \
        "ERROR: 1st geometric_heliocentric_position() test doesn't match"

    assert abs(round(lat, 4) - 0.6141) < TOL, \
        "ERROR: 2nd geometric_heliocentric_position() test doesn't match"

    assert abs(round(r, 5) - 10.06266) < TOL, \
        "ERROR: 3rd geometric_heliocentric_position() test doesn't match"


def test_saturn_orbital_elements_mean_equinox():
    """Tests the orbital_elements_mean_equinox() method of Saturn class"""

    epoch = Epoch(2065, 6, 24.0)
    l, a, e, i, ome, arg = Saturn(epoch).orbital_elements_mean_equinox()

    assert abs(round(l, 6) - 131.196871) < TOL, \
        "ERROR: 1st orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(a, 8) - 9.55490779) < TOL, \
        "ERROR: 2nd orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(e, 7) - 0.0553209) < TOL, \
        "ERROR: 3rd orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(i, 6) - 2.486426) < TOL, \
        "ERROR: 4th orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(ome, 5) - 114.23974) < TOL, \
        "ERROR: 5th orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(arg, 6) - (-19.896331)) < TOL, \
        "ERROR: 6th orbital_elements_mean_equinox() test doesn't match"


def test_saturn_orbital_elements_j2000():
    """Tests the orbital_elements_j2000() method of Saturn class"""

    epoch = Epoch(2065, 6, 24.0)
    l, a, e, i, ome, arg = Saturn(epoch).orbital_elements_j2000()

    assert abs(round(l, 6) - 130.28188) < TOL, \
        "ERROR: 1st orbital_elements_j2000() test doesn't match"

    assert abs(round(a, 8) - 9.55490779) < TOL, \
        "ERROR: 2nd orbital_elements_j2000() test doesn't match"

    assert abs(round(e, 7) - 0.0553209) < TOL, \
        "ERROR: 3rd orbital_elements_j2000() test doesn't match"

    assert abs(round(i, 6) - 2.490529) < TOL, \
        "ERROR: 4th orbital_elements_j2000() test doesn't match"

    assert abs(round(ome, 5) - 113.49736) < TOL, \
        "ERROR: 5th orbital_elements_j2000() test doesn't match"

    assert abs(round(arg, 6) - (-20.068943)) < TOL, \
        "ERROR: 6th orbital_elements_j2000() test doesn't match"


def test_saturn_geocentric_position():
    """Tests the geocentric_position() method of Saturn class"""

    epoch = Epoch(1992, 12, 20.0)
    constellation = Constellation(Earth(epoch), Saturn(epoch))
    ra, dec, elon = constellation.geocentric_position()

    assert ra.ra_str(n_dec=1) == "21h 11' 41.8''", \
        "ERROR: 1st geocentric_position() test doesn't match"

    assert dec.dms_str(n_dec=1) == "-17d 15' 40.8''", \
        "ERROR: 2nd geocentric_position() test doesn't match"

    assert elon.dms_str(n_dec=1) == "46d 51' 47.7''", \
        "ERROR: 3rd geocentric_position() test doesn't match"


def test_saturn_conjunction():
    """Tests the conjunction() method of Saturn class"""

    epoch = Epoch(2125, 6, 1.0)
    conjunction = Saturn(epoch).conjunction()
    y, m, d = conjunction.get_date()

    assert abs(round(y, 0) - 2125) < TOL, \
        "ERROR: 1st conjunction() test doesn't match"

    assert abs(round(m, 0) - 8) < TOL, \
        "ERROR: 2nd conjunction() test doesn't match"

    assert abs(round(d, 4) - 26.4035) < TOL, \
        "ERROR: 3rd conjunction() test doesn't match"


def test_saturn_opposition():
    """Tests the opposition() method of Saturn class"""

    epoch = Epoch(-6, 9, 1.0)
    oppo = Saturn(epoch).opposition()
    y, m, d = oppo.get_date()

    assert abs(round(y, 0) - (-6)) < TOL, \
        "ERROR: 1st opposition() test doesn't match"

    assert abs(round(m, 0) - 9) < TOL, \
        "ERROR: 2nd opposition() test doesn't match"

    assert abs(round(d, 4) - 14.3709) < TOL, \
        "ERROR: 3rd opposition() test doesn't match"


def test_saturn_station_longitude_1():
    """Tests the station_longitude_1() method of Saturn class"""

    epoch = Epoch(2018, 11, 1.0)
    sta1 = Saturn(epoch).station_longitude_1()
    y, m, d = sta1.get_date()

    assert abs(round(y, 0) - 2018) < TOL, \
        "ERROR: 1st station_longitude_1() test doesn't match"

    assert abs(round(m, 0) - 4) < TOL, \
        "ERROR: 2nd station_longitude_1() test doesn't match"

    assert abs(round(d, 4) - 17.9433) < TOL, \
        "ERROR: 3rd station_longitude_1() test doesn't match"


def test_saturn_station_longitude_2():
    """Tests the station_longitude_2() method of Saturn class"""

    epoch = Epoch(2018, 11, 1.0)
    sta2 = Saturn(epoch).station_longitude_2()
    y, m, d = sta2.get_date()

    assert abs(round(y, 0) - 2018) < TOL, \
        "ERROR: 1st station_longitude_2() test doesn't match"

    assert abs(round(m, 0) - 9) < TOL, \
        "ERROR: 2nd station_longitude_2() test doesn't match"

    assert abs(round(d, 4) - 6.4175) < TOL, \
        "ERROR: 3rd station_longitude_2() test doesn't match"


def test_saturn_perihelion_aphelion():
    """Tests the perihelion_aphelion() method of Saturn class"""

    epoch = Epoch(2030, 1, 1.0)
    e = Saturn(epoch).perihelion()
    y, m, d, h, mi, s = e.get_full_date()

    assert abs(y - 2032) < TOL, \
        "ERROR: 1st perihelion_aphelion() test doesn't match"

    assert abs(m - 11) < TOL, \
        "ERROR: 2nd perihelion_aphelion() test doesn't match"

    assert abs(d - 28) < TOL, \
        "ERROR: 3rd perihelion_aphelion() test doesn't match"

    epoch = Epoch(1925, 1, 1.0)
    e = Saturn(epoch).aphelion()
    y, m, d, h, mi, s = e.get_full_date()

    assert abs(y - 1929) < TOL, \
        "ERROR: 4th perihelion_aphelion() test doesn't match"

    assert abs(m - 11) < TOL, \
        "ERROR: 5th perihelion_aphelion() test doesn't match"

    assert abs(d - 11) < TOL, \
        "ERROR: 6th perihelion_aphelion() test doesn't match"


def test_saturn_passage_nodes():
    """Tests the passage_nodes() method of Saturn class"""

    epoch = Epoch(2019, 1, 1)
    time, r = Saturn(epoch).passage_nodes()
    y, m, d = time.get_date()
    d = round(d, 1)
    r = round(r, 4)

    assert abs(y - 2034) < TOL, \
        "ERROR: 1st passage_nodes() test doesn't match"

    assert abs(m - 5) < TOL, \
        "ERROR: 2nd passage_nodes() test doesn't match"

    assert abs(d - 30.2) < TOL, \
        "ERROR: 3rd passage_nodes() test doesn't match"

    assert abs(r - 9.0546) < TOL, \
        "ERROR: 4th passage_nodes() test doesn't match"
