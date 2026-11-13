# (class, book, part-slug, order, title, icon, questions)
# question ~ correct ~ wrong1 ~ wrong2 ~ wrong3 ~ explanation
B6 = 'Ganita Prakash'
B7a, B7b = 'Ganita Prakash Part 1', 'Ganita Prakash Part 2'
B8a, B8b = 'Ganita Prakash Part 1', 'Ganita Prakash Part 2'

DATA = [
# ---------------- CLASS 6 ----------------
(6, B6, '', 1, 'Patterns in Mathematics', '🔢', """
What is the next number in the sequence 1, 4, 9, 16, 25, …?~36~30~35~49~These are square numbers: 1², 2², 3², 4², 5², so the next is 6² = 36.
What is the sum of the first 5 odd numbers (1 + 3 + 5 + 7 + 9)?~25~20~24~30~The sum of the first n odd numbers is n², so 5² = 25.
The triangular numbers are 1, 3, 6, 10, 15, … What comes next?~21~20~25~18~Add 6 to the previous term: 15 + 6 = 21.
In the sequence 1, 2, 3, 5, 8, 13, … each number is the sum of the two before it. What is the next number?~21~18~20~26~8 + 13 = 21 (Virahanka–Fibonacci numbers).
The sum of two consecutive triangular numbers (like 3 + 6) is always a ____.~square number~prime number~cube number~even number~3 + 6 = 9, 6 + 10 = 16, 10 + 15 = 25. All are squares.
What is the next term in 2, 4, 8, 16, …?~32~24~30~20~Each term is double the previous term, so 16 × 2 = 32.
"""),
(6, B6, '', 2, 'Lines and Angles', '📐', """
How many degrees are there in a straight angle?~180°~90°~360°~120°~A straight angle forms a straight line and measures 180°.
An angle that measures less than 90° is called ____.~acute~obtuse~right~reflex~Acute angles lie between 0° and 90°.
An angle of 135° is a(n) ____ angle.~obtuse~acute~right~straight~Obtuse angles lie between 90° and 180°.
How many right angles make one complete turn?~4~2~3~6~4 × 90° = 360°, a full turn.
Two lines in a plane that never meet, however far extended, are called ____ lines.~parallel~intersecting~perpendicular~curved~Parallel lines always stay the same distance apart and never meet.
How many end points does a ray have?~1~2~0~3~A ray starts at one point and goes on endlessly in one direction.
"""),
(6, B6, '', 3, 'Number Play', '🎲', """
In the Collatz rule (halve if even, 3n + 1 if odd), which number follows 3?~10~4~9~6~3 is odd, so 3 × 3 + 1 = 10.
Which of these numbers is a palindrome?~121~123~132~213~121 reads the same forwards and backwards.
What is the smallest 3-digit palindrome?~101~100~111~121~101 is the smallest 3-digit number that reads the same both ways.
Using the digits 1, 2, 3, 4 once each, what is the greatest 4-digit number?~4321~1234~4312~3421~Arrange the digits from largest to smallest.
What is the sum 1 + 2 + 3 + … + 10?~55~50~45~65~Pair the numbers: 5 pairs of 11 gives 55.
What is the smallest 4-digit number that can be made from 3, 0, 5, 7 using each digit once?~3057~0357~3075~3507~A number cannot start with 0, so start with 3, then use 0, 5, 7 in increasing order.
"""),
(6, B6, '', 4, 'Data Handling and Presentation', '📊', """
In a pictograph, data is shown using ____.~pictures or symbols~only numbers~only lines~only tables~A pictograph uses symbols to represent a number of items.
How many items does a tally group of five (four lines struck through by a fifth) show?~5~4~6~10~The fifth line crosses the four to make a group of 5.
What is the mean (average) of 4, 6 and 8?~6~5~7~8~(4 + 6 + 8) ÷ 3 = 18 ÷ 3 = 6.
What is the range of the data 3, 9, 5, 12, 2?~10~9~12~14~Range = greatest − smallest = 12 − 2 = 10.
A bar graph is mostly used to ____.~compare quantities~measure angles~draw shapes~count digits~The height or length of each bar shows the value of a category.
The number of times a value occurs in the data is called its ____.~frequency~range~mean~scale~Frequency means how often a value appears.
"""),
(6, B6, '', 5, 'Prime Time', '🔑', """
What is the smallest prime number?~2~1~3~0~2 has exactly two factors, 1 and 2, and it is the smallest prime.
Which of these numbers is prime?~29~21~27~39~29 has only the factors 1 and 29. The others are divisible by 3.
What is the prime factorisation of 36?~2² × 3²~2 × 3 × 6~2³ × 3~4 × 9~36 = 2 × 2 × 3 × 3.
The number 1 is ____.~neither prime nor composite~prime~composite~both prime and composite~1 has only one factor, so it is neither prime nor composite.
Which pair is a pair of twin primes?~11 and 13~13 and 15~7 and 11~17 and 21~Twin primes differ by 2 and are both prime. 11 and 13 qualify.
Which pair of numbers is co-prime?~8 and 15~6 and 9~10 and 15~12 and 18~8 and 15 have no common factor other than 1.
"""),
(6, B6, '', 6, 'Perimeter and Area', '📏', """
What is the perimeter of a square with side 7 cm?~28 cm~14 cm~49 cm~21 cm~Perimeter = 4 × side = 4 × 7 = 28 cm.
What is the area of a rectangle 8 cm long and 5 cm wide?~40 cm²~26 cm²~13 cm²~45 cm²~Area = length × breadth = 8 × 5 = 40 cm².
What is the perimeter of a rectangle with length 10 cm and breadth 4 cm?~28 cm~40 cm~14 cm~24 cm~Perimeter = 2 × (10 + 4) = 28 cm.
What is the area of a square of side 9 m?~81 m²~36 m²~18 m²~72 m²~Area = side × side = 9 × 9 = 81 m².
A rectangle has an area of 48 cm² and a length of 8 cm. What is its breadth?~6 cm~5 cm~7 cm~8 cm~Breadth = area ÷ length = 48 ÷ 8 = 6 cm.
What is the area of a triangle with base 6 cm and height 4 cm?~12 cm²~24 cm²~10 cm²~20 cm²~Area = ½ × base × height = ½ × 6 × 4 = 12 cm².
"""),
(6, B6, '', 7, 'Fractions', '🍕', """
What is ½ + ¼?~3/4~2/6~2/3~1/4~½ = 2/4, and 2/4 + 1/4 = 3/4.
Which fraction is equivalent to ⅔?~4/6~3/4~2/5~6/8~Multiply the top and bottom of 2/3 by 2 to get 4/6.
Which of these is an improper fraction?~7/4~3/7~2/5~1/8~An improper fraction has a numerator greater than or equal to its denominator.
What is 5/6 − 1/6?~2/3~4/12~1/3~1/6~(5 − 1)/6 = 4/6 = 2/3.
Which fraction is greater, 3/5 or 2/3?~2/3~3/5~They are equal~Cannot be compared~3/5 = 9/15 and 2/3 = 10/15, so 2/3 is greater.
Written as an improper fraction, 1¾ is ____.~7/4~5/4~6/4~13/4~1¾ = (1 × 4 + 3)/4 = 7/4.
"""),
(6, B6, '', 8, 'Playing with Constructions', '✏️', """
Which instrument is used to draw a circle?~Compass~Protractor~Set square~Ruler~A compass draws circles and arcs.
The radius of a circle is the distance from ____.~the centre to any point on the circle~one edge to the other through the centre~one point on the circle to another~the centre to outside the circle~All points on a circle are the same distance from the centre.
If the radius of a circle is 5 cm, its diameter is ____.~10 cm~5 cm~2.5 cm~15 cm~Diameter = 2 × radius = 10 cm.
What is the measure of each angle of a rectangle?~90°~60°~45°~180°~All four angles of a rectangle are right angles.
Which instrument is used to measure an angle?~Protractor~Compass~Divider~Ruler~A protractor measures angles in degrees.
A square has ____.~4 equal sides and 4 right angles~2 pairs of unequal sides~3 equal sides~only 1 right angle~A square is a regular quadrilateral.
"""),
(6, B6, '', 9, 'Symmetry', '🦋', """
How many lines of symmetry does a square have?~4~1~2~8~A square has 2 diagonals, 1 vertical and 1 horizontal line of symmetry.
How many lines of symmetry does an equilateral triangle have?~3~1~2~6~There is one line from each vertex to the middle of the opposite side.
Which letter has a vertical line of symmetry?~A~F~G~R~Only A looks the same on both sides of a vertical line.
How many lines of symmetry does a rectangle (that is not a square) have?~2~4~1~0~One vertical and one horizontal line.
How many lines of symmetry does a circle have?~Infinitely many~1~2~4~Every line through the centre is a line of symmetry.
What is the order of rotational symmetry of an equilateral triangle?~3~1~2~6~It looks the same after turns of 120°, 240° and 360°.
"""),
(6, B6, '', 10, 'The Other Side of Zero', '🌡️', """
What is the opposite (additive inverse) of +5?~−5~0~5~−1/5~5 + (−5) = 0.
Which is greater, −2 or −7?~−2~−7~They are equal~Cannot say~On a number line, −2 lies to the right of −7.
What is −3 + 5?~2~−2~8~−8~Start at −3 and move 5 steps right to reach 2.
What is 4 − 9?~−5~5~13~−13~4 − 9 = −5.
Numbers to the left of zero on the number line are ____.~negative~positive~zero~fractions only~Negative integers lie to the left of 0.
The temperature falls from 3 °C to −4 °C. By how much did it fall?~7 °C~1 °C~−7 °C~4 °C~3 − (−4) = 7 degrees.
"""),
# ---------------- CLASS 7 PART 1 ----------------
(7, B7a, 'p1', 1, 'Large Numbers Around Us', '🌐', """
How many thousands make one lakh?~100~10~1000~10,000~1 lakh = 1,00,000 = 100 × 1000.
1 crore equals how many lakhs?~100~10~1000~10,000~1 crore = 1,00,00,000 = 100 lakh.
10 million is equal to ____.~1 crore~10 lakh~10 crore~1 lakh~10 million = 1,00,00,000 = 1 crore.
What is the smallest 8-digit number?~1,00,00,000~10,00,000~99,99,999~1,00,000~It is 1 crore.
What is 99,999 + 1?~1,00,000~10,000~9,99,999~1,000~Adding 1 to the greatest 5-digit number gives 1 lakh.
4,86,000 rounded to the nearest lakh is ____.~5,00,000~4,00,000~4,90,000~6,00,000~86,000 is more than half a lakh, so round up to 5 lakh.
"""),
(7, B7a, 'p1', 2, 'Arithmetic Expressions', '🧮', """
What is 18 + 6 × 4 − 12 ÷ 3?~38~28~36~60~Multiply and divide first: 18 + 24 − 4 = 38.
In BODMAS, which operation is done first?~Brackets~Division~Addition~Subtraction~Brackets come first.
What is 5 + 3 × 2?~11~16~13~10~Multiply first: 3 × 2 = 6, then 5 + 6 = 11.
Where should brackets be placed so that 5 + 3 × 2 = 16?~(5 + 3) × 2~5 + (3 × 2)~(5 + 3 × 2)~5 + 3 × (2)~(5 + 3) × 2 = 8 × 2 = 16.
What is 100 − (20 + 30) ÷ 5?~90~10~80~70~(20 + 30) = 50, 50 ÷ 5 = 10, 100 − 10 = 90.
What is 2 × 3²?~18~36~12~9~Evaluate the power first: 3² = 9, then 2 × 9 = 18.
"""),
(7, B7a, 'p1', 3, 'A Peek Beyond the Point', '🔹', """
0.375 written as a fraction in simplest form is ____.~3/8~375/100~3/5~5/8~0.375 = 375/1000 = 3/8.
Which is the correct ascending order of 0.3, 0.03, 0.303, 0.033?~0.03, 0.033, 0.3, 0.303~0.03, 0.3, 0.033, 0.303~0.3, 0.303, 0.03, 0.033~0.033, 0.03, 0.303, 0.3~Compare place by place: 0.03 < 0.033 < 0.3 < 0.303.
What is 0.5 + 0.25?~0.75~0.30~0.55~0.525~0.50 + 0.25 = 0.75.
What is the place value of 7 in 3.472?~Hundredths~Tenths~Thousandths~Units~In 3.472 the digits after the point are tenths 4, hundredths 7, thousandths 2.
What is 2.5 × 4?~10~8~12.5~9~2.5 × 4 = 10.
What is 3/4 as a decimal?~0.75~0.34~0.25~0.80~3 ÷ 4 = 0.75.
"""),
(7, B7a, 'p1', 4, 'Expressions using Letter-Numbers', '🔤', """
Which expression means "7 more than twice a number x"?~2x + 7~7x + 2~2(x + 7)~x + 14~Twice x is 2x, and 7 more gives 2x + 7.
What is the value of 3a − 2b + c when a = 2, b = 1, c = 4?~8~12~6~4~3(2) − 2(1) + 4 = 6 − 2 + 4 = 8.
What is the perimeter of a square of side a?~4a~a²~2a~a + 4~A square has 4 equal sides.
Which pair are like terms?~3x and 5x~3x and 5y~2x and x²~4 and 4x~Like terms have the same letter part.
Simplify 4n + 3n.~7n~12n~7n²~n~Add the coefficients: 4 + 3 = 7.
If n is a number, which expression gives the next number?~n + 1~n − 1~2n~n²~The successor of n is n + 1.
"""),
(7, B7a, 'p1', 5, 'Parallel and Intersecting Lines', '↔️', """
When two lines intersect, vertically opposite angles are ____.~equal~supplementary~complementary~always 90°~Vertically opposite angles are always equal.
The sum of angles in a linear pair is ____.~180°~90°~360°~270°~Adjacent angles on a straight line add up to 180°.
Two lines intersect and one angle is 60°. What is the vertically opposite angle?~60°~120°~30°~90°~Vertically opposite angles are equal.
A transversal is a line that ____.~cuts two or more lines at distinct points~is parallel to a line~is the longest line~touches a circle~A transversal crosses other lines at different points.
When two parallel lines are cut by a transversal, corresponding angles are ____.~equal~supplementary~complementary~unrelated~Corresponding angles are equal for parallel lines.
What is the complement of 35°?~55°~145°~65°~35°~Complementary angles add to 90°, so 90° − 35° = 55°.
"""),
(7, B7a, 'p1', 6, 'Number Play', '🎯', """
The sum of three consecutive numbers is always divisible by ____.~3~2~4~5~n + (n+1) + (n+2) = 3n + 3 = 3(n + 1).
A number is divisible by 3 if ____.~the sum of its digits is divisible by 3~its last digit is 3~its last digit is even~it is odd~This is the divisibility rule for 3.
Which number is divisible by 9?~729~731~842~955~7 + 2 + 9 = 18, which is divisible by 9.
A number is divisible by 4 if its last two digits form a number divisible by ____.~4~2~8~5~100 is divisible by 4, so only the last two digits matter.
What is the sum of an even and an odd number?~Odd~Even~Prime~Zero~For example 4 + 3 = 7, which is odd.
What is the sum of the first 6 odd numbers?~36~21~30~42~The sum of the first n odd numbers is n², and 6² = 36.
"""),
(7, B7a, 'p1', 7, 'A Tale of Three Intersecting Lines', '🔺', """
What is the sum of the angles of a triangle?~180°~90°~270°~360°~The angles of any triangle add up to 180°.
Which set of sides can form a triangle?~5 cm, 7 cm, 10 cm~3 cm, 4 cm, 8 cm~2 cm, 3 cm, 6 cm~1 cm, 2 cm, 3 cm~The sum of any two sides must be greater than the third side: 5 + 7 > 10.
An exterior angle of a triangle equals the ____.~sum of the two opposite interior angles~third angle~difference of the angles~half of the sum of all angles~This is the exterior angle property.
Two angles of a triangle are 50° and 60°. What is the third angle?~70°~80°~60°~110°~180° − 50° − 60° = 70°.
What is each angle of an equilateral triangle?~60°~90°~45°~30°~180° ÷ 3 = 60°.
An isosceles triangle has a vertex angle of 40°. What is each base angle?~70°~140°~40°~80°~(180° − 40°) ÷ 2 = 70°.
"""),
(7, B7a, 'p1', 8, 'Working with Fractions', '🥧', """
What is 2/3 × 3/4?~1/2~6/7~5/7~2/4~(2 × 3)/(3 × 4) = 6/12 = 1/2.
What is 3/4 ÷ 1/2?~3/2~3/8~1/2~2/3~Dividing by 1/2 is the same as multiplying by 2: 3/4 × 2 = 3/2.
What is 1/2 of 3/5?~3/10~4/7~3/7~1/10~1/2 × 3/5 = 3/10.
What is the reciprocal of 5/7?~7/5~5/7~−5/7~1~The reciprocal flips numerator and denominator.
What is 2/5 ÷ 4?~1/10~8/5~1/5~4/10~2/5 × 1/4 = 2/20 = 1/10.
A ribbon 3/4 m long is cut into pieces of 1/8 m each. How many pieces are there?~6~4~8~3~3/4 ÷ 1/8 = 3/4 × 8 = 6.
"""),
# ---------------- CLASS 7 PART 2 ----------------
(7, B7b, 'p2', 1, 'Geometric Twins', '👯', """
Two figures with exactly the same shape and size are ____.~congruent~similar only~parallel~symmetric~Congruent figures overlap exactly.
Which rule says two triangles are congruent if three sides of one equal three sides of the other?~SSS~AAA~SSA~AAS only~SSS stands for Side-Side-Side.
In the SAS rule, the angle must be ____.~between the two given sides~opposite one side~outside the triangle~any angle~It must be the included angle.
Which is NOT a rule for congruence of triangles?~AAA~SSS~SAS~ASA~Equal angles alone give a similar triangle, not necessarily a congruent one.
Two squares with side 5 cm each are ____.~congruent~not congruent~only similar~different in shape~Same shape and same size means congruent.
In congruent triangles, corresponding parts are ____.~equal~different~double~parallel~Corresponding sides and angles are equal.
"""),
(7, B7b, 'p2', 2, 'Operations with Integers', '➕', """
What is (−3) × (−4)?~12~−12~7~−7~A negative times a negative is positive.
What is (−6) × 5?~−30~30~−11~11~A negative times a positive is negative.
What is (−20) ÷ (−5)?~4~−4~25~−25~A negative divided by a negative is positive.
What is 15 ÷ (−3)?~−5~5~−45~12~A positive divided by a negative is negative.
What is (−2) × (−2) × (−2)?~−8~8~−6~6~(−2) × (−2) = 4, and 4 × (−2) = −8.
What is (−7) × 0?~0~−7~7~Undefined~Anything multiplied by zero is zero.
"""),
(7, B7b, 'p2', 3, 'Finding Common Ground', '🤝', """
What is the HCF of 12 and 18?~6~3~36~2~The greatest number that divides both 12 and 18 is 6.
What is the LCM of 4 and 6?~12~24~2~10~The smallest common multiple of 4 and 6 is 12.
The HCF of 6 and 8 is 2 and their LCM is 24. What is HCF × LCM?~48~14~32~12~2 × 24 = 48, which equals 6 × 8.
What is the LCM of the co-prime numbers 3 and 5?~15~8~1~5~For co-prime numbers, the LCM is the product.
What is the HCF of 15 and 25?~5~3~15~75~Both are divisible by 5, and there is no larger common divisor.
What is the largest number that divides both 24 and 36 exactly?~12~6~4~72~HCF(24, 36) = 12.
"""),
(7, B7b, 'p2', 4, 'Another Peek Beyond the Point', '🔸', """
What is 0.6 × 0.4?~0.24~2.4~0.024~0.64~6 × 4 = 24, with two decimal places gives 0.24.
What is 1.5 ÷ 0.5?~3~0.3~30~0.75~Multiply both by 10: 15 ÷ 5 = 3.
What is 2.4 ÷ 4?~0.6~6~0.06~0.8~24 ÷ 4 = 6, so 2.4 ÷ 4 = 0.6.
What is 0.25 × 100?~25~2.5~250~0.025~Moving the decimal two places right gives 25.
What is 3.6 ÷ 0.12?~30~3~0.3~300~360 ÷ 12 = 30.
What is 0.2 × 0.2?~0.04~0.4~0.004~0.22~2 × 2 = 4 with two decimal places gives 0.04.
"""),
(7, B7b, 'p2', 5, 'Connecting the Dots…', '📈', """
What is the mean of 5, 7, 9 and 11?~8~7~9~10~(5 + 7 + 9 + 11) ÷ 4 = 32 ÷ 4 = 8.
What is the median of 3, 7 and 5?~5~3~7~15~Sorted: 3, 5, 7. The middle value is 5.
What is the mode of 2, 3, 3, 4, 5?~3~2~4~5~3 occurs most often.
What is the median of 2, 4, 6, 8?~5~4~6~20~The middle two values are 4 and 6, so the median is their mean, 5.
What is the range of 12, 7, 19, 3?~16~15~22~9~Range = 19 − 3 = 16.
Which graph is best for comparing the sales of five shops?~Bar graph~Number line~Protractor~Compass~A bar graph compares values across categories.
"""),
(7, B7b, 'p2', 6, 'Constructions and Tilings', '🧩', """
Which two instruments are mainly needed to construct a triangle with given sides?~Ruler and compass~Protractor and set square only~Divider and eraser~Pencil only~Arcs drawn with a compass fix the third vertex.
Which regular polygon cannot tile a plane by itself?~Regular pentagon~Equilateral triangle~Square~Regular hexagon~The interior angle of 108° does not divide 360° evenly.
What is the interior angle of an equilateral triangle?~60°~90°~120°~45°~All three angles are equal and add to 180°.
What is each interior angle of a regular hexagon?~120°~60°~108°~135°~(6 − 2) × 180° ÷ 6 = 120°.
What is the sum of the angles around a point?~360°~180°~90°~720°~A full turn is 360°.
To construct a triangle with sides 4 cm, 5 cm and 6 cm, which rule do you use?~SSS~SAS~ASA~RHS~All three sides are known.
"""),
(7, B7b, 'p2', 7, 'Finding the Unknown', '❓', """
Solve x + 5 = 12.~x = 7~x = 17~x = 5~x = 12~Subtract 5 from both sides.
Solve 3x = 21.~x = 7~x = 18~x = 63~x = 24~Divide both sides by 3.
Solve 2x − 3 = 9.~x = 6~x = 3~x = 12~x = 4.5~2x = 12, so x = 6.
Solve x/4 = 5.~x = 20~x = 1.25~x = 9~x = 4~Multiply both sides by 4.
Solve 5x + 2 = 27.~x = 5~x = 4~x = 6~x = 29~5x = 25, so x = 5.
The sum of a number and 8 is 15. What is the number?~7~23~8~15~x + 8 = 15, so x = 7.
"""),
# ---------------- CLASS 8 PART 1 ----------------
(8, B8a, 'p1', 1, 'A Square and A Cube', '🧊', """
What is 15²?~225~150~30~255~15 × 15 = 225.
What is the cube root of 27?~3~9~27~6~3 × 3 × 3 = 27.
What is √144?~12~14~72~11~12 × 12 = 144.
What is 5³?~125~15~75~25~5 × 5 × 5 = 125.
By what smallest number should 12 be multiplied to get a perfect square?~3~2~4~6~12 = 2² × 3, so multiply by 3 to get 36.
Which of these is a perfect cube?~216~100~250~300~216 = 6³.
"""),
(8, B8a, 'p1', 2, 'Power Play', '⚡', """
What is 2⁵?~32~10~25~64~2 × 2 × 2 × 2 × 2 = 32.
Simplify 3² × 3⁴.~3⁶~3⁸~9⁶~3¹⁶~When multiplying powers with the same base, add the exponents.
What is (−7)⁰?~1~0~−7~7~Any non-zero number raised to the power 0 is 1.
What is 10⁻² as a fraction?~1/100~−100~1/20~100~A negative exponent means the reciprocal: 1/10².
What is (2³)²?~64~32~16~128~(2³)² = 2⁶ = 64.
What is 45,000 in standard form?~4.5 × 10⁴~45 × 10³~4.5 × 10³~0.45 × 10⁴~Move the decimal point 4 places: 4.5 × 10⁴.
"""),
(8, B8a, 'p1', 3, 'A Story of Numbers', '📜', """
What number does the Roman numeral XIV represent?~14~16~6~24~X = 10 and IV = 4, so XIV = 14.
Which Roman numeral stands for 50?~L~C~D~V~L is 50, C is 100, D is 500.
What is the key feature of the Hindu–Arabic number system?~Place value with a symbol for zero~Only tally marks~Only letters~No symbols~Place value and zero allow any number to be written with ten digits.
What is 5 written in binary (base 2)?~101~110~11~111~5 = 4 + 0 + 1 = 101₂.
What number does the Roman numeral IX represent?~9~11~4~6~I before X means 1 less than 10.
Which digits are used in the binary number system?~0 and 1~0 to 7~1 and 2~0 to 9~Base 2 uses only 0 and 1.
"""),
(8, B8a, 'p1', 4, 'Quadrilaterals', '🔷', """
What is the sum of the interior angles of a quadrilateral?~360°~180°~270°~540°~A quadrilateral can be divided into 2 triangles, so 2 × 180° = 360°.
Which quadrilateral has all sides equal and all angles 90°?~Square~Rhombus~Rectangle~Trapezium~A square has equal sides and right angles.
The diagonals of a rhombus ____.~bisect each other at right angles~are equal~are parallel~do not meet~This is a property of a rhombus.
The diagonals of a rectangle are ____.~equal~perpendicular~parallel~unequal~In a rectangle, both diagonals have the same length.
In a parallelogram, adjacent angles are ____.~supplementary~equal~complementary~right angles~Adjacent angles add up to 180°.
A trapezium has ____.~exactly one pair of parallel sides~two pairs of parallel sides~no parallel sides~four equal sides~This is the definition of a trapezium.
"""),
(8, B8a, 'p1', 5, 'Number Play', '🧠', """
Which number is divisible by 11?~1331~1332~1334~1337~For 1331, alternating digit sum is 1 − 3 + 3 − 1 = 0.
The sum of a 2-digit number and its reverse (for example 25 + 52) is always divisible by ____.~11~7~9~5~It equals 11 × (sum of the digits): 25 + 52 = 77.
What is Kaprekar's constant?~6174~1729~1089~9999~Repeatedly applying Kaprekar's process on 4-digit numbers reaches 6174.
A number is divisible by 6 if it is divisible by ____.~both 2 and 3~both 2 and 4~both 3 and 4~5 and 6~6 = 2 × 3, and 2 and 3 are co-prime.
What is the last digit of 7²?~9~7~4~1~7² = 49.
Which of these cannot be the last digit of a perfect square?~2~1~4~9~Squares end in 0, 1, 4, 5, 6 or 9 only.
"""),
(8, B8a, 'p1', 6, 'We Distribute, Yet Things Multiply', '✖️', """
What is (x + y)²?~x² + 2xy + y²~x² + y²~x² + xy + y²~2x + 2y~Expand (x + y)(x + y).
What is (a + b)(a − b)?~a² − b²~a² + b²~a² − 2ab + b²~2a~This is the difference of squares identity.
What is (x + 3)(x + 2)?~x² + 5x + 6~x² + 6~x² + 5x + 5~2x + 5~x² + 2x + 3x + 6 = x² + 5x + 6.
What is 3(x + 4)?~3x + 12~3x + 4~x + 12~12x~Distribute 3 over both terms.
What is 101 × 99 using identities?~9999~10,001~9,899~10,099~(100 + 1)(100 − 1) = 100² − 1 = 9999.
What is (x − 1)²?~x² − 2x + 1~x² − 1~x² + 2x + 1~x² − 2x − 1~(x − 1)² = x² − 2x + 1.
"""),
(8, B8a, 'p1', 7, 'Proportional Reasoning-1', '⚖️', """
What is the ratio 12 : 18 in simplest form?~2 : 3~3 : 2~6 : 9 only~4 : 5~Divide both by 6.
If 5 pens cost ₹40, what do 8 pens cost?~₹64~₹48~₹56~₹80~One pen costs ₹8, so 8 pens cost ₹64.
Divide ₹100 in the ratio 2 : 3. What is the larger share?~₹60~₹40~₹50~₹70~3 out of 5 parts: 3/5 × 100 = ₹60.
In direct proportion, when one quantity increases, the other ____.~increases in the same ratio~decreases~stays the same~becomes zero~Direct proportion means both change by the same factor.
If 1 kg of sugar costs ₹60, what do 2.5 kg cost?~₹150~₹120~₹135~₹180~60 × 2.5 = ₹150.
On a map with scale 1 : 100, a length of 5 cm shows an actual length of ____.~5 m~50 cm~500 m~0.5 m~5 × 100 = 500 cm = 5 m.
"""),
# ---------------- CLASS 8 PART 2 ----------------
(8, B8b, 'p2', 1, 'Fractions in Disguise', '💯', """
What is 25% of 80?~20~25~40~16~25/100 × 80 = 20.
Written as a percentage, 3/4 is ____.~75%~34%~25%~80%~3/4 = 75/100.
20% is equal to the fraction ____.~1/5~1/4~2/5~1/2~20/100 = 1/5.
What is 200 increased by 10%?~220~210~190~202~10% of 200 is 20, so 200 + 20 = 220.
A ₹500 item has a 20% discount. What is the selling price?~₹400~₹480~₹450~₹100~Discount = ₹100, so price = 500 − 100 = ₹400.
Cost price is ₹200 and selling price is ₹250. What is the profit percentage?~25%~20%~50%~10%~Profit ₹50 ÷ 200 × 100 = 25%.
"""),
(8, B8b, 'p2', 2, 'The Baudhayana-Pythagoras Theorem', '📐', """
The legs of a right triangle are 3 and 4. What is the hypotenuse?~5~6~7~12~3² + 4² = 25, and √25 = 5.
Which set is a Pythagorean triplet?~5, 12, 13~4, 5, 6~6, 7, 8~2, 3, 4~5² + 12² = 169 = 13².
The hypotenuse is the side ____.~opposite the right angle~adjacent to the right angle~shortest~parallel to the base~It is always the longest side of a right triangle.
Is a triangle with sides 6, 8, 10 right-angled?~Yes~No~Only if isosceles~Cannot say~6² + 8² = 100 = 10².
What is the diagonal of a square of side 1?~√2~2~1~√3~1² + 1² = 2, so diagonal = √2.
In a right triangle, hypotenuse is 13 and one leg is 5. What is the other leg?~12~8~10~11~13² − 5² = 169 − 25 = 144, so the leg is 12.
"""),
(8, B8b, 'p2', 3, 'Proportional Reasoning-2', '🔁', """
6 workers finish a job in 10 days. How many days will 12 workers take?~5~20~15~10~More workers means fewer days: 6 × 10 = 12 × days.
In inverse proportion, the ____ of the two quantities stays constant.~product~sum~difference~quotient~If x increases, y decreases so that xy stays the same.
A car at 60 km/h takes 4 hours. At 80 km/h, how long will it take?~3 hours~5 hours~4 hours~2 hours~Distance 240 km ÷ 80 = 3 hours.
Which pair of quantities is in inverse proportion (distance fixed)?~Speed and time~Time and distance~Cost and weight~Length and area~Distance = speed × time is constant.
Food lasts 20 days for 10 people. How long will it last for 20 people?~10 days~40 days~20 days~5 days~Double the people means half the days.
If xy = 24 and x = 4, what is y?~6~20~96~4~y = 24 ÷ 4 = 6.
"""),
(8, B8b, 'p2', 4, 'Exploring Some Geometric Themes', '🧱', """
How many faces does a cube have?~6~4~8~12~A cube has 6 square faces.
How many edges does a cube have?~12~6~8~10~A cube has 12 edges.
Euler's formula for polyhedra says F + V − E equals ____.~2~0~1~3~For a cube: 6 + 8 − 12 = 2.
How many faces does a triangular prism have?~5~4~6~3~It has 2 triangular and 3 rectangular faces.
How many vertices does a square pyramid have?~5~4~6~8~There are 4 base vertices and 1 apex.
A net of a cube is made of ____.~6 squares~4 squares~8 squares~6 triangles~A cube has 6 square faces.
"""),
(8, B8b, 'p2', 5, 'Tales by Dots and Lines', '📉', """
In the point (3, 4), the x-coordinate is ____.~3~4~7~12~The first number of the ordered pair is the x-coordinate.
What are the coordinates of the origin?~(0, 0)~(1, 1)~(0, 1)~(1, 0)~The origin is where the two axes meet.
Which graph is best for showing change over time?~Line graph~Pictograph~Tally chart~Venn diagram~A line graph shows trends over time.
A point on the x-axis has y-coordinate ____.~0~1~equal to x~undefined~Every point on the x-axis has the form (x, 0).
The point (5, 0) lies on the ____.~x-axis~y-axis~origin~neither axis~The y-coordinate is 0.
The horizontal axis of a graph is called the ____.~x-axis~y-axis~z-axis~origin~The x-axis runs left to right.
"""),
(8, B8b, 'p2', 6, 'Algebra Play', '🎮', """
Solve 2x + 5 = 15.~x = 5~x = 10~x = 7.5~x = 20~2x = 10, so x = 5.
Solve 3(x − 2) = 12.~x = 6~x = 4~x = 10~x = 2~x − 2 = 4, so x = 6.
What is the coefficient of x in 7x − 3?~7~−3~3~4~The coefficient is the number multiplying x.
If x = 3, what is the value of x² + 2x?~15~12~9~18~9 + 6 = 15.
Solve x/2 + 3 = 7.~x = 8~x = 5~x = 2~x = 20~x/2 = 4, so x = 8.
In a linear equation in one variable, the highest power of the variable is ____.~1~2~0~3~That is what makes it linear.
"""),
(8, B8b, 'p2', 7, 'Area', '🟩', """
What is the area of a triangle with base 10 cm and height 6 cm?~30 cm²~60 cm²~16 cm²~36 cm²~½ × 10 × 6 = 30 cm².
What is the area of a parallelogram with base 8 cm and height 5 cm?~40 cm²~13 cm²~20 cm²~80 cm²~Area = base × height = 8 × 5 = 40.
What is the area of a trapezium with parallel sides 6 cm and 10 cm and height 4 cm?~32 cm²~64 cm²~24 cm²~16 cm²~½ × (6 + 10) × 4 = 32.
What is the area of a rhombus with diagonals 8 cm and 6 cm?~24 cm²~48 cm²~14 cm²~28 cm²~½ × d₁ × d₂ = ½ × 8 × 6 = 24.
What is the area of a square whose diagonal is 10 cm?~50 cm²~100 cm²~25 cm²~20 cm²~Area = ½ × d² = ½ × 100 = 50.
1 m² is equal to how many cm²?~10,000~100~1000~1,00,000~1 m = 100 cm, so 1 m² = 100 × 100 cm².
"""),
]
