# (class, book, part-slug, order, title, icon, questions)
# question ~ correct ~ wrong1 ~ wrong2 ~ wrong3 ~ explanation
B9 = 'Ganita Manjari Part 1'
B10 = 'NCERT Mathematics'

DATA = [
# ---------------- CLASS 9 (Ganita Manjari, Part 1) ----------------
(9, B9, '', 1, 'Orienting Yourself: The Use of Coordinates', '🧭', """
In which quadrant does the point (3, −2) lie?~Fourth~First~Second~Third~x is positive and y is negative, which is the fourth quadrant.
What is the distance between (0, 0) and (3, 4)?~5~7~4~12~√(3² + 4²) = √25 = 5.
What is the midpoint of (2, 4) and (6, 8)?~(4, 6)~(8, 12)~(2, 2)~(3, 5)~Average the coordinates: ((2 + 6)/2, (4 + 8)/2).
The point (0, 5) lies on the ____.~y-axis~x-axis~origin~first quadrant~Every point with x = 0 lies on the y-axis.
What is the reflection of (3, 2) in the x-axis?~(3, −2)~(−3, 2)~(−3, −2)~(2, 3)~Reflecting in the x-axis changes the sign of y only.
What is the abscissa of the point (−4, 7)?~−4~7~3~−7~The abscissa is the x-coordinate.
"""),
(9, B9, '', 2, 'Introduction to Linear Polynomials', '📈', """
What is the degree of the polynomial 3x + 5?~1~0~2~3~The highest power of x is 1.
What is the zero of the polynomial 2x − 6?~3~−3~6~2~2x − 6 = 0 gives x = 3.
If p(x) = 4x − 1, what is p(2)?~7~8~9~5~4(2) − 1 = 7.
The graph of y = 2x + 1 is ____.~a straight line~a parabola~a circle~a pair of lines~A linear polynomial gives a straight-line graph.
What is the zero of x + 7?~−7~7~0~1~x + 7 = 0 gives x = −7.
In y = mx + c, the constant c is the ____.~y-intercept~slope~x-intercept~origin~c is the value of y when x = 0.
"""),
(9, B9, '', 3, 'The World of Numbers', '🔢', """
Which of these numbers is irrational?~√2~0.5~22/7~−3~√2 cannot be written as a fraction of integers.
The decimal 0.333… equals which fraction?~1/3~3/10~33/100~1/33~0.333… = 1/3, which is rational.
Which of these is an irrational number?~π~0.75~√49~5/8~π is non-terminating and non-repeating.
Which of these is a rational number between 1 and 2?~3/2~√5~π~√3~3/2 = 1.5 lies between 1 and 2.
The decimal expansion of a rational number is ____.~terminating or non-terminating recurring~non-terminating non-recurring~always terminating~always recurring~This characterises rational numbers.
What is (√3)²?~3~9~√9~6~Squaring a square root gives the original number.
"""),
(9, B9, '', 4, 'Exploring Algebraic Identities', '🧮', """
What is (a + b)²?~a² + 2ab + b²~a² + b²~a² − 2ab + b²~2a + 2b~Expand (a + b)(a + b).
What is (x − y)²?~x² − 2xy + y²~x² + y²~x² − y²~x² + 2xy + y²~(x − y)² = x² − 2xy + y².
What is (x + 2)(x − 2)?~x² − 4~x² + 4~x² − 2~x² − 4x~This is the (a + b)(a − b) = a² − b² identity.
What is 103² using an identity?~10609~10609 + 1~10600~10309~(100 + 3)² = 10000 + 600 + 9 = 10609.
If x + y = 5 and xy = 6, what is x² + y²?~13~25~11~31~x² + y² = (x + y)² − 2xy = 25 − 12 = 13.
How do you factorise x² − 9?~(x − 3)(x + 3)~(x − 9)(x + 1)~(x − 3)²~(x + 3)²~Difference of squares.
"""),
(9, B9, '', 5, "I'm Up and Down, and Round and Round", '⭕', """
The longest chord of a circle is its ____.~diameter~radius~tangent~arc~A diameter passes through the centre and is the longest chord.
A perpendicular from the centre of a circle to a chord ____.~bisects the chord~is equal to the radius~makes the chord longer~is parallel to it~This is a standard circle theorem.
Equal chords of a circle are ____ from the centre.~equidistant~at different distances~always 0 distance~twice~Equal chords are the same distance from the centre.
What is the angle in a semicircle?~90°~180°~60°~45°~The angle subtended by a diameter on the circle is a right angle.
The angle subtended by an arc at the centre is ____ the angle at any point on the remaining circle.~twice~half~equal to~three times~This is the central angle theorem.
What is the circumference of a circle of radius 7 cm (π = 22/7)?~44 cm~154 cm~22 cm~14 cm~2πr = 2 × 22/7 × 7 = 44.
"""),
(9, B9, '', 6, 'Measuring Space: Perimeter and Area', '📏', """
What is the area of a rectangle 12 m by 5 m?~60 m²~34 m²~17 m²~120 m²~12 × 5 = 60.
What is the area of a circle of radius 7 cm (π = 22/7)?~154 cm²~44 cm²~49 cm²~22 cm²~πr² = 22/7 × 49 = 154.
What is the perimeter of a square of side 9 m?~36 m~18 m~81 m~27 m~4 × 9 = 36.
What is the area of a triangle with base 10 cm and height 8 cm?~40 cm²~80 cm²~18 cm²~48 cm²~½ × 10 × 8 = 40.
What is the circumference of a circle of radius 14 cm (π = 22/7)?~88 cm~44 cm~616 cm~28 cm~2πr = 2 × 22/7 × 14 = 88.
1 hectare equals ____.~10,000 m²~1000 m²~100 m²~1,00,000 m²~1 hectare = 100 m × 100 m.
"""),
(9, B9, '', 7, 'The Mathematics of Maybe: Introduction to Probability', '🎰', """
The probability of any event always lies between ____.~0 and 1~−1 and 1~0 and 100~1 and 2~Probability is never negative and never greater than 1.
What is the probability of getting a head in one toss of a fair coin?~1/2~1~1/4~0~There are two equally likely outcomes.
A die is rolled. What is the probability of getting a prime number?~1/2~1/3~2/3~1/6~Primes on a die are 2, 3, 5, which is 3 out of 6.
The sum of the probabilities of all outcomes of an experiment is ____.~1~0~2~100~All possible outcomes together make a sure event.
The probability of an impossible event is ____.~0~1~1/2~−1~It can never happen.
A bag has 3 red and 2 blue balls. What is the probability of drawing a red ball?~3/5~2/5~1/2~3/2~3 favourable out of 5.
"""),
(9, B9, '', 8, 'Predicting What Comes Next: Exploring Sequences and Progressions', '🔮', """
In the AP 2, 5, 8, 11, … what is the common difference?~3~2~5~11~Each term is 3 more than the previous.
What is the 10th term of the AP 3, 7, 11, …?~39~43~40~37~a + 9d = 3 + 9 × 4 = 39.
What is the common ratio of the GP 2, 6, 18, …?~3~4~2~6~6 ÷ 2 = 3.
What is the next term in the GP 3, 6, 12, …?~24~18~15~36~Each term is multiplied by 2.
What is the sum of the first 10 natural numbers?~55~45~100~50~n(n + 1)/2 = 55.
What is the 8th term of the AP 5, 9, 13, …?~33~37~29~45~5 + 7 × 4 = 33.
"""),
# ---------------- CLASS 10 ----------------
(10, B10, '', 1, 'Real Numbers', '🔢', """
What is the HCF of 26 and 91?~13~7~26~2~26 = 2 × 13 and 91 = 7 × 13.
The Fundamental Theorem of Arithmetic says every composite number ____.~can be expressed as a product of primes in a unique way~is always even~is always a perfect square~cannot be factorised~Unique prime factorisation, apart from the order of factors.
Which of these is irrational?~2 + √3~22/7~0.25~√81~The sum of a rational and an irrational number is irrational.
What is the LCM of 6 and 20?~60~120~30~40~6 = 2 × 3 and 20 = 2² × 5, so LCM = 2² × 3 × 5 = 60.
HCF(a, b) = 4, LCM(a, b) = 60 and a = 12. What is b?~20~15~48~5~HCF × LCM = a × b, so 240 = 12 × b.
Euclid's division lemma states that for positive integers a and b, a = bq + r where ____.~0 ≤ r < b~0 < r ≤ b~r > b~r = b~The remainder is less than the divisor.
"""),
(10, B10, '', 2, 'Polynomials', '📉', """
What are the zeros of x² − 5x + 6?~2 and 3~−2 and −3~1 and 6~−1 and −6~x² − 5x + 6 = (x − 2)(x − 3).
The graph of a quadratic polynomial is a ____.~parabola~straight line~circle~hyperbola~Quadratic polynomials give a U-shaped curve.
For ax² + bx + c, the sum of the zeros is ____.~−b/a~b/a~c/a~−c/a~This is the standard relation.
For ax² + bx + c, the product of the zeros is ____.~c/a~−c/a~b/a~−b/a~This is the standard relation.
Which quadratic polynomial has zeros 2 and −3?~x² + x − 6~x² − x − 6~x² + 5x + 6~x² − 5x − 6~Sum = −1 and product = −6, so x² − (sum)x + product = x² + x − 6.
What is the maximum number of zeros a cubic polynomial can have?~3~2~1~4~A polynomial of degree n has at most n zeros.
"""),
(10, B10, '', 3, 'Pair of Linear Equations in Two Variables', '⚖️', """
Solve x + y = 5 and x − y = 1.~x = 3, y = 2~x = 2, y = 3~x = 4, y = 1~x = 5, y = 0~Adding gives 2x = 6, so x = 3 and y = 2.
If two lines are parallel, the pair of equations has ____.~no solution~one solution~two solutions~infinitely many solutions~Parallel lines never meet.
A consistent pair of linear equations has ____.~a unique solution or infinitely many solutions~no solution~exactly two solutions~only zero as a solution~Consistent means at least one solution exists.
If a₁/a₂ = b₁/b₂ = c₁/c₂, the lines are ____.~coincident~parallel~intersecting~perpendicular~The equations represent the same line.
If x + y = 14 and x − y = 4, what is x?~9~10~5~7~Adding gives 2x = 18, so x = 9.
If x = 2 satisfies 3x + y = 10, what is y?~4~2~16~−4~6 + y = 10, so y = 4.
"""),
(10, B10, '', 4, 'Quadratic Equations', '🧩', """
What are the roots of x² − 5x + 6 = 0?~2 and 3~−2 and −3~1 and 6~5 and 1~(x − 2)(x − 3) = 0.
The discriminant of ax² + bx + c = 0 is ____.~b² − 4ac~b² + 4ac~4ac − b²~√(b² − 4ac)~D = b² − 4ac.
When are the roots of a quadratic equation real and equal?~D = 0~D > 0~D < 0~a = 0~Equal roots occur when the discriminant is zero.
Does 2x² − 4x + 3 = 0 have real roots?~No, because D = −8~Yes, two distinct roots~Yes, equal roots~Cannot be found~D = 16 − 24 = −8 < 0.
What are the roots of x² − 9 = 0?~3 and −3~9 and −9~3 only~0 and 9~x² = 9 gives x = ±3.
The quadratic formula gives x = ____.~(−b ± √(b² − 4ac)) / 2a~(b ± √(b² − 4ac)) / a~−b / 2a only~(−b ± b² − 4ac) / 2a~This is the standard formula.
"""),
(10, B10, '', 5, 'Arithmetic Progressions', '🪜', """
What is the 10th term of the AP 2, 7, 12, …?~47~52~42~57~a + 9d = 2 + 9 × 5 = 47.
What is the sum of the first 20 natural numbers?~210~200~420~190~n(n + 1)/2 = 20 × 21/2 = 210.
What is the common difference of 7, 3, −1, …?~−4~4~3~−3~3 − 7 = −4.
For the AP 5, 8, 11, …, which term is 35?~11th~10th~12th~9th~5 + (n − 1)3 = 35 gives n = 11.
What is the sum of the first 10 odd natural numbers?~100~55~110~90~The sum of the first n odd numbers is n².
If aₙ = 3n + 2, what is a₅?~17~15~14~20~3 × 5 + 2 = 17.
"""),
(10, B10, '', 6, 'Triangles', '🔺', """
Two triangles are similar if ____.~their corresponding angles are equal and sides are proportional~they have the same area~they have the same perimeter~they are both right-angled~This defines similar triangles.
The Basic Proportionality Theorem says a line parallel to one side of a triangle ____.~divides the other two sides in the same ratio~bisects the triangle~is equal to the third side~is perpendicular to the base~This is also called Thales' theorem.
Two similar triangles have sides in the ratio 2 : 3. What is the ratio of their areas?~4 : 9~2 : 3~8 : 27~3 : 2~The ratio of areas equals the square of the ratio of sides.
A right triangle has legs 6 and 8. What is the hypotenuse?~10~14~12~9~6² + 8² = 100.
Which criterion proves that two triangles are similar when two angles of one equal two angles of the other?~AA~SSS~RHS~SAS~Angle-Angle similarity.
In △ABC, DE ∥ BC with AD = 2, DB = 3 and AE = 4. What is EC?~6~8/3~3~5~AD/DB = AE/EC gives 2/3 = 4/EC, so EC = 6.
"""),
(10, B10, '', 7, 'Coordinate Geometry', '🗺️', """
What is the distance between (1, 2) and (4, 6)?~5~7~4~25~√(3² + 4²) = 5.
What is the midpoint of (2, 3) and (8, 7)?~(5, 5)~(10, 10)~(6, 4)~(3, 2)~((2 + 8)/2, (3 + 7)/2) = (5, 5).
Which point divides (0, 0) and (6, 0) in the ratio 1 : 2?~(2, 0)~(3, 0)~(4, 0)~(1, 0)~x = (1 × 6 + 2 × 0)/3 = 2.
What is the distance of (−5, 12) from the origin?~13~17~7~169~√(25 + 144) = √169 = 13.
What is the area of the triangle with vertices (0, 0), (4, 0) and (0, 3)?~6~12~7~3.5~½ × 4 × 3 = 6.
Points (1, 1), (2, 2) and (3, 3) are ____.~collinear~vertices of a right triangle~vertices of an equilateral triangle~vertices of a square~All three lie on the line y = x.
"""),
(10, B10, '', 8, 'Introduction to Trigonometry', '📐', """
What is sin 30°?~1/2~√3/2~1~1/√2~This is a standard value.
What is tan 45°?~1~0~√3~1/√3~Opposite and adjacent sides are equal in a 45° right triangle.
sin²θ + cos²θ = ____.~1~0~2~tan²θ~This is the basic trigonometric identity.
If sin θ = 3/5 and θ is acute, what is cos θ?~4/5~3/4~5/4~5/3~Using a 3-4-5 right triangle.
cosec θ equals ____.~1/sin θ~1/cos θ~cos θ/sin θ~sin θ/cos θ~Cosecant is the reciprocal of sine.
sec²θ − tan²θ = ____.~1~0~−1~sin²θ~This is an identity derived from sin²θ + cos²θ = 1.
"""),
(10, B10, '', 9, 'Some Applications of Trigonometry', '🗼', """
The angle of elevation is measured from the ____.~horizontal up to the line of sight~vertical down to the object~ground to the sun only~line of sight down to the horizontal~It is the angle you look up above the horizontal.
A 10 m ladder makes an angle of 30° with the ground. How high does it reach on the wall?~5 m~10 m~5√3 m~20 m~Height = 10 sin 30° = 5 m.
A tower 10 m high casts a shadow 10 m long. What is the angle of elevation of the sun?~45°~30°~60°~90°~tan θ = 10/10 = 1, so θ = 45°.
A tower is 10√3 m high and you stand 10 m from its base. What is the angle of elevation of its top?~60°~30°~45°~90°~tan θ = √3, so θ = 60°.
The angle of depression from the top of a building to a point on the ground equals the angle of elevation from that point to the top because ____.~they are alternate angles~they are supplementary~they are vertical angles~they are complementary~Parallel horizontal lines create equal alternate angles.
A 15 m high tower makes an angle of elevation of 30° at a point. What is the distance of the point from its base?~15√3 m~15/√3 m~7.5 m~30 m~tan 30° = 15/d, so d = 15√3.
"""),
(10, B10, '', 10, 'Circles', '⭕', """
A tangent to a circle meets the circle at ____.~exactly one point~two points~no point~infinitely many points~That is the definition of a tangent.
The tangent at a point of a circle is ____ to the radius through that point.~perpendicular~parallel~equal~at 45°~The tangent is perpendicular to the radius at the point of contact.
Tangents drawn from an external point to a circle are ____.~equal in length~perpendicular~parallel~of different lengths~The two tangent segments are equal.
A point is 13 cm from the centre of a circle of radius 5 cm. What is the length of the tangent from it?~12 cm~8 cm~18 cm~√194 cm~√(13² − 5²) = √144 = 12.
How many tangents can be drawn from a point inside a circle?~None~One~Two~Infinite~Every line through an interior point cuts the circle.
How many tangents can be drawn from an external point?~Two~One~Three~Infinite~Exactly two tangents exist.
"""),
(10, B10, '', 11, 'Areas Related to Circles', '🥧', """
What is the area of a circle of radius 7 cm (π = 22/7)?~154 cm²~44 cm²~22 cm²~49 cm²~πr² = 154.
What is the area of a sector of angle 90° in a circle of radius 14 cm (π = 22/7)?~154 cm²~616 cm²~308 cm²~77 cm²~(90/360) × 22/7 × 14² = 154.
What is the length of an arc of a 60° sector with radius 21 cm (π = 22/7)?~22 cm~44 cm~66 cm~11 cm~(60/360) × 2 × 22/7 × 21 = 22.
What is the area of a semicircle of radius 14 cm (π = 22/7)?~308 cm²~616 cm²~154 cm²~44 cm²~½ × 22/7 × 196 = 308.
The area of a quadrant of a circle of radius 7 cm is ____ (π = 22/7).~38.5 cm²~154 cm²~77 cm²~19.25 cm²~¼ × 154 = 38.5.
The formula for the area of a sector with angle θ is ____.~(θ/360) × πr²~(θ/360) × 2πr~θ × πr²~(360/θ) × πr²~A sector is a fraction θ/360 of the circle.
"""),
(10, B10, '', 12, 'Surface Areas and Volumes', '🧊', """
What is the volume of a cylinder of radius 7 cm and height 10 cm (π = 22/7)?~1540 cm³~440 cm³~154 cm³~3080 cm³~πr²h = 22/7 × 49 × 10 = 1540.
What is the volume of a cone of radius 7 cm and height 3 cm (π = 22/7)?~154 cm³~462 cm³~49 cm³~22 cm³~⅓πr²h = ⅓ × 22/7 × 49 × 3 = 154.
What is the surface area of a sphere of radius r?~4πr²~2πr²~πr²~(4/3)πr³~Surface area of a sphere is 4πr².
What is the total surface area of a cube of side a?~6a²~4a²~a³~12a~A cube has 6 square faces.
What is the curved surface area of a cylinder of radius 7 cm and height 10 cm (π = 22/7)?~440 cm²~1540 cm²~220 cm²~154 cm²~2πrh = 2 × 22/7 × 7 × 10 = 440.
What is the total surface area of a solid hemisphere of radius r?~3πr²~2πr²~4πr²~πr²~Curved surface 2πr² plus flat base πr².
"""),
(10, B10, '', 13, 'Statistics', '📊', """
For grouped data, the mean is ____.~Σfx / Σf~Σx / n only~Σf / Σfx~Σf × Σx~Mean is the sum of frequency times class mark divided by total frequency.
The empirical relation between the three measures of central tendency is ____.~Mode = 3 Median − 2 Mean~Mode = 2 Median − 3 Mean~Mean = 3 Median − 2 Mode~Median = 3 Mode − 2 Mean~This is the standard relation.
What is the median of 3, 5, 7, 9, 11?~7~5~9~35~The middle value of five ordered numbers is the third one.
The modal class is the class with the ____.~highest frequency~lowest frequency~largest class mark~smallest width~The mode lies in the class that occurs most often.
What is the mean of 10, 20 and 30?~20~30~15~60~(10 + 20 + 30)/3 = 20.
To find the median of grouped data, you look for the class whose cumulative frequency is ____.~just greater than n/2~equal to n~less than n/4~equal to zero~That is the median class.
"""),
(10, B10, '', 14, 'Probability', '🎲', """
What is the probability of a sure event?~1~0~1/2~100~A sure event always happens.
A fair die is rolled. What is the probability of getting an even number?~1/2~1/3~2/3~1/6~Even numbers are 2, 4, 6, so 3 out of 6.
If P(E) = 0.3, what is P(not E)?~0.7~0.3~1.3~0~P(E) + P(not E) = 1.
A card is drawn from a pack of 52 cards. What is the probability that it is a king?~1/13~1/4~4/13~1/52~4 kings out of 52 cards.
Two coins are tossed. What is the probability of getting two heads?~1/4~1/2~1/3~3/4~One outcome (HH) out of four.
A bag has 4 red and 6 green balls. What is the probability of drawing a green ball?~3/5~2/5~6/4~1/6~6 out of 10 balls are green.
"""),
]
