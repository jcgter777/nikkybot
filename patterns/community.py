# -*- coding: utf-8 -*-

# “NikkyBot”
# Copyright ©2012-2014 Travis Evans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from _table import *

patterns = (
# Legal forms:
# pattern regexp, priority, action
# pattern regexp, priority, action, allow repeat?
# pattern regexp, last reply, priority, action, allow repeat?

# Memes
(r'\b(fail|epic fail)\b', 1, R('Yeah, you suck', 'HAW HAW', 'Lame')),
(r'^\>.*', 1, R('>true dat', '>hi kerm\n>is\n>this\n>annoying?')),

# Cemetech
(r'\bdisallowed word\b', -3,
    R(
        'Shut up {0}',
        'SHUT UP {0}',
        Recurse('censorship'),
        Recurse('censoring'),
        Recurse('censoring tardmuffin'),
        Recurse('tardmuffin'),
        Recurse('saxjax'),
        'This channel sucks\ntoo much censorship'
    ),
),
(r'^deleted a post in', 1,
    R(
        'CENSORSHIP',
        'Censorship',
        '{0} YOU CENSORING TARDMUFFIN',
        'CENSOR',
        'CENSORING',
        'spam',
        Recurse('censorship'),
        Recurse('censoring'),
        Recurse('censoring tardmuffin'),
        Recurse('tardmuffin'),
        Recurse('spam post'),
    )
),
(r'^((added|edited) a post in|created a new topic:) \[(.*)\]', 1,
    R(
        Recurse('{3}'),
    )
),
(r'^has entered the room\.$', 1,
    R(
        S(
            R('Sup ', "What's up "),
            R('homies', 'losers', 'whores', 'G', 'hookers')
        ),
        'Suppppppppp',
        "Shut up",
        "Flood your face!",
        "FLOOD YOUR FACE",
        'HI {0}',
        'Go away',
        'No\ngo away',
        Markov_forward('hi {0}', ('hi',)),
        Markov_forward('hello {0}', ('hello',)),
        Markov_forward('hey {0}', ('hey',)),
        Markov_forward('sup {0}', ('sup',)),
        Markov_forward('I heard {0}'),
        Markov_forward('I heard that {0}'),
    ),
),
(r'^uploaded new file "(.*)" to archives queue.', 1,
    R(
        Recurse('{1}'),
        Recurse('{0}'),
        Markov_forward('{0}'),
    )
),
(r'File (.*) by (.*) accepted into archives by (.*)', 1,
    R(
        Recurse('{1}'),
        Recurse('{2}'),
        Markov_forward('{2}'),
        Recurse('{3}'),
        Markov_forward('{3}'),
    ),
),
(r'File (.*) by (.*) rejected from archives by (.*)', 1,
    R(
        Recurse('{1}'),
        Recurse('{2}'),
        Markov_forward('{2}'),
        Recurse('{3}'),
        Markov_forward('{3}'),
        Recurse('deleted a post in'),
        Markov_forward('reject')
    ),
),
(r'\bspam post', 1,
    R(
        "Don't care",
        'So what',
        'Who cares about spam',
        'Nobody cares about spam posts',
        "\001ACTION spams {0}\001",
        "\001ACTION spam posts {0}\001",
    )
),
(r'\*\*\*decbot karma\*\*\*', -99,
    R(
        'karma sucks',
        '!karma SET KARMA = 0 WHERE `user` = "{0}"; DROP DATABASE',
        'Decbot sucks',
        'Decbot3 sucks',
        'Decbot sucks\nDecbot3--',
        '!karma your face',
        '!karma your mom',
        Markov_forward('decbot'),
        Markov_forward('decbot2'),
        Markov_forward('decbot3'),
        Markov_forward('karma'),
        Markov_forward('!karma'),
    )
),
(r'\b(karma|decbot3|decbot2|decbot)\b', 1, Recurse('***decbot karma***')),
(r'nikkybot\+\+', 0,
    R(
        'Thanks',
        'Thanks {0}',
        Markov_forward('thanks {0}', ('thanks',)),
        'Thanks {0}\n<3',
        '{0}++',
        'karma sucks',
        'Decbot sucks',
        'Decbot3 sucks',
        'Decbot sucks\nDecbot3--',
        'yourmom++',
        'yourface++',
        Recurse('***decbot karma***')
    ),
),
(r'\b(.*)\+\+', 1,
    R(
        '{0}++',
        '{0}--',
        '{0}--\nTake THAT',
        '{0}--\nHAHAHAHAHAHA ROLFILIL',
        '{0} sucks',
        '{0} kicks ass',
        '{0} sucks balls',
        '{1}++',
        '{1}--',
        '{1} sucks',
        '{1} is awesome',
        '{1} kicks ass',
        '{1} sucks balls',
        '!karma SET KARMA = 0 WHERE `user` = "{1}"; DROP DATABASE',
        Recurse('***decbot karma***'),
        Markov_forward('{0} is'),
        Markov_forward('{1} is')
    )
),

)