# (class, book, part-slug, order, title, icon, questions)
# question ~ correct ~ wrong1 ~ wrong2 ~ wrong3 ~ explanation
B = 'NCERT Mathematics'

DATA = [
# ---------------- CLASS 11 ----------------
(11, B, '', 1, 'Sets', '🔵', """
If n(A) = 10, n(B) = 8 and n(A ∩ B) = 3, what is n(A ∪ B)?~15~18~21~11~n(A ∪ B) = 10 + 8 − 3 = 15.
How many elements does the power set of a set with 3 elements have?~8~6~9~3~The power set has 2ⁿ elements, so 2³ = 8.
If A = {1, 2, 3} and B = {3, 4}, what is A ∩ B?~{3}~{1, 2, 3, 4}~{1, 2}~{4}~Only 3 is common to both.
How many subsets does the set {a, b} have?~4~2~3~1~2² = 4: ∅, {a}, {b}, {a, b}.
According to De Morgan's law, (A ∪ B)′ = ____.~A′ ∩ B′~A′ ∪ B′~A ∩ B~A − B~The complement of a union is the intersection of complements.
If A = {1, 2, 3, 4} and B = {2, 4}, what is A − B?~{1, 3}~{2, 4}~{1, 2, 3, 4}~{}~A − B contains elements in A but not in B.
"""),
(11, B, '', 2, 'Relations and Functions', '🔗', """
If n(A) = 3 and n(B) = 4, how many elements are in A × B?~12~7~81~64~n(A × B) = 3 × 4 = 12.
What is the domain of f(x) = √(x − 2)?~x ≥ 2~x > 2~x ≤ 2~All real numbers~The expression under the root must be non-negative.
What is the range of f(x) = x² for x ∈ ℝ?~[0, ∞)~(−∞, ∞)~(0, ∞)~(−∞, 0]~Squares are never negative.
If A has 2 elements and B has 3 elements, how many relations from A to B are there?~64~6~8~9~Relations are subsets of A × B, and 2⁶ = 64.
If f(x) = 2x + 1, what is f(3)?~7~6~5~9~2(3) + 1 = 7.
A function from A to B assigns ____.~exactly one element of B to each element of A~at least one element of B to each element of A~two elements of A to B~nothing~Every input has exactly one output.
"""),
(11, B, '', 3, 'Trigonometric Functions', '🌊', """
π radians equals ____.~180°~90°~360°~270°~π rad = 180°.
60° in radians is ____.~π/3~π/6~π/2~2π/3~60 × π/180 = π/3.
sin 2A = ____.~2 sin A cos A~2 sin A~sin²A − cos²A~2 cos A~This is the double angle formula.
What is the period of sin x?~2π~π~π/2~4π~sin(x + 2π) = sin x.
cos(−θ) = ____.~cos θ~−cos θ~sin θ~−sin θ~Cosine is an even function.
What is the range of sin x?~[−1, 1]~(−1, 1)~[0, 1]~(−∞, ∞)~The sine function never goes beyond −1 and 1.
"""),
(11, B, '', 4, 'Complex Numbers and Quadratic Equations', '🧿', """
i² = ____.~−1~1~i~−i~By definition, i = √(−1).
What is (2 + 3i) + (1 − i)?~3 + 2i~3 + 4i~1 + 2i~3 − 2i~Add real parts and imaginary parts separately.
What is |3 + 4i|?~5~7~25~1~√(3² + 4²) = 5.
What is the conjugate of 5 − 2i?~5 + 2i~−5 + 2i~−5 − 2i~2 − 5i~Change the sign of the imaginary part.
What is i⁷?~−i~i~1~−1~i⁷ = i⁴ · i³ = 1 · (−i).
What is (1 + i)²?~2i~2~1 + 2i~0~1 + 2i + i² = 2i.
"""),
(11, B, '', 5, 'Linear Inequalities', '↕️', """
What happens to the inequality sign when both sides are multiplied by a negative number?~It reverses~It stays the same~It becomes equal~It disappears~For example, 2 < 3 but −2 > −3.
What is the solution of 2x + 3 > 7?~x > 2~x < 2~x > 5~x > 4~2x > 4, so x > 2.
x ≥ 3 can be written as the interval ____.~[3, ∞)~(3, ∞)~(−∞, 3]~(−∞, 3)~The square bracket includes 3.
What is the solution of |x| < 2?~−2 < x < 2~x < 2~x > −2 or x < 2~x > 2 or x < −2~|x| < a means −a < x < a.
What is the solution of −3x < 9?~x > −3~x < −3~x > 3~x < 3~Dividing by −3 reverses the inequality.
What is the solution of 3x − 5 ≤ 4?~x ≤ 3~x ≥ 3~x ≤ 1~x ≥ 1~3x ≤ 9, so x ≤ 3.
"""),
(11, B, '', 6, 'Permutations and Combinations', '🎰', """
What is 5!?~120~25~60~24~5 × 4 × 3 × 2 × 1 = 120.
What is ⁵P₂?~20~10~25~40~5 × 4 = 20.
What is ⁵C₂?~10~20~5~25~5!/(2! × 3!) = 10.
In how many ways can the letters of the word ABC be arranged?~6~3~9~12~3! = 6.
Which of these is true?~⁸C₃ = ⁸C₅~⁸C₃ = ⁸C₄~⁸C₃ = ⁸C₆~⁸C₃ = ⁸C₇~ⁿCᵣ = ⁿCₙ₋ᵣ.
In how many ways can the letters of the word LEVEL be arranged?~30~120~60~15~5!/(2! × 2!) = 30.
"""),
(11, B, '', 7, 'Binomial Theorem', '🔡', """
How many terms are there in the expansion of (x + y)ⁿ?~n + 1~n~n − 1~2n~The terms run from r = 0 to r = n.
What is the coefficient of x² in (1 + x)⁵?~10~5~20~1~⁵C₂ = 10.
The general term Tᵣ₊₁ in (a + b)ⁿ is ____.~ⁿCᵣ aⁿ⁻ʳ bʳ~ⁿCᵣ aʳ bʳ~ⁿPᵣ aⁿ⁻ʳ bʳ~ⁿCᵣ₊₁ aⁿ⁻ʳ bʳ~This is the standard formula.
What is the sum of the coefficients in the expansion of (1 + x)⁴?~16~8~4~32~Put x = 1 to get 2⁴.
Which term is the middle term in the expansion of (a + b)⁶?~4th~3rd~5th~6th~With 7 terms in total, the middle one is the 4th.
What is the third term in the expansion of (1 + x)³ in increasing powers of x?~3x²~3x~x³~1~(1 + x)³ = 1 + 3x + 3x² + x³.
"""),
(11, B, '', 8, 'Sequences and Series', '➗', """
What is the sum 1 + 2 + 3 + … + 10?~55~50~45~100~n(n + 1)/2 = 55.
What is the sum of the infinite GP 1 + 1/2 + 1/4 + …?~2~1~3/2~4~a/(1 − r) = 1/(1 − 1/2) = 2.
What is the geometric mean of 4 and 16?~8~10~9~64~√(4 × 16) = 8.
In an AP with a = 2 and d = 3, what is the 5th term?~14~17~11~12~a + 4d = 14.
What is the common ratio of 3, −6, 12, …?~−2~2~−3~3~−6 ÷ 3 = −2.
For positive numbers, which inequality is true?~AM ≥ GM~AM ≤ GM~AM < GM~AM = GM always~This is the AM–GM inequality.
"""),
(11, B, '', 9, 'Straight Lines', '📏', """
What is the slope of the line through (1, 2) and (3, 6)?~2~1/2~4~3~(6 − 2)/(3 − 1) = 2.
The slope-intercept form of a line is ____.~y = mx + c~x/a + y/b = 1~y − y₁ = m~ax + by = 0~m is the slope and c is the y-intercept.
What is the slope of a line perpendicular to a line with slope 2?~−1/2~1/2~−2~2~The product of the slopes of perpendicular lines is −1.
What is the distance of the line 3x + 4y − 5 = 0 from the origin?~1~5~5/7~0~|−5|/√(9 + 16) = 1.
What is the equation of the line through the origin with slope 3?~y = 3x~y = x + 3~y = 3~x = 3y~y − 0 = 3(x − 0).
What is the slope of the x-axis?~0~1~∞~−1~The x-axis is horizontal.
"""),
(11, B, '', 10, 'Conic Sections', '🌀', """
What is the eccentricity of a circle?~0~1~less than 1 but positive~greater than 1~A circle is a conic with e = 0.
What is the radius of the circle x² + y² = 25?~5~25~√5~10~r² = 25 gives r = 5.
What is the focus of the parabola y² = 8x?~(2, 0)~(8, 0)~(4, 0)~(0, 2)~y² = 4ax with 4a = 8 gives a = 2.
The eccentricity of an ellipse is ____.~less than 1~equal to 1~greater than 1~equal to 0 always~For an ellipse, 0 < e < 1.
The eccentricity of a hyperbola is ____.~greater than 1~less than 1~equal to 1~equal to 0~For a hyperbola, e > 1.
What is the length of the major axis of x²/25 + y²/9 = 1?~10~5~6~3~a² = 25, so a = 5 and the major axis is 2a = 10.
"""),
(11, B, '', 11, 'Introduction to Three Dimensional Geometry', '🧭', """
Into how many octants do the three coordinate planes divide space?~8~4~6~3~Each axis divides space into two parts, giving 2 × 2 × 2 = 8.
What is the distance between (1, 2, 3) and (4, 6, 15)?~13~12~15~169~√(9 + 16 + 144) = 13.
Which form do the coordinates of a point on the z-axis take?~(0, 0, z)~(x, 0, 0)~(0, y, 0)~(x, y, 0)~The x and y coordinates are zero.
What is the distance of the point (2, 3, 6) from the origin?~7~11~5~49~√(4 + 9 + 36) = 7.
What is the midpoint of (2, 4, 6) and (4, 6, 8)?~(3, 5, 7)~(6, 10, 14)~(1, 1, 1)~(2, 3, 4)~Average each coordinate.
How many coordinate planes are there?~3~2~4~6~The xy, yz and zx planes.
"""),
(11, B, '', 12, 'Limits and Derivatives', '📉', """
What is the limit of x² as x → 2?~4~2~0~8~Substitute x = 2.
What is d/dx (x³)?~3x²~x²~3x~x⁴/4~d/dx xⁿ = n xⁿ⁻¹.
What is lim (x → 0) sin x / x?~1~0~∞~−1~This is a standard limit.
What is d/dx (sin x)?~cos x~−cos x~−sin x~tan x~The derivative of sine is cosine.
What is the derivative of a constant?~0~1~the constant itself~undefined~A constant does not change.
What is d/dx (5x² + 3x)?~10x + 3~5x + 3~10x² + 3~10x~Differentiate each term separately.
"""),
(11, B, '', 13, 'Statistics', '📊', """
The variance is the ____ of the standard deviation.~square~square root~double~half~Variance = (SD)².
What is the mean of 2, 4, 6, 8, 10?~6~5~8~30~30 ÷ 5 = 6.
What is the range of the data 5, 9, 2, 14, 7?~12~9~7~14~14 − 2 = 12.
What is the standard deviation of a data set in which every value is the same?~0~1~the value itself~undefined~There is no deviation from the mean.
The coefficient of variation is ____.~(σ / mean) × 100~(mean / σ) × 100~σ × mean~σ − mean~It measures relative variability in percent.
What is the variance of the numbers 1, 2, 3?~2/3~1~2~1/3~Mean = 2, and (1 + 0 + 1)/3 = 2/3.
"""),
(11, B, '', 14, 'Probability', '🎲', """
How many outcomes are in the sample space when two coins are tossed?~4~2~3~8~HH, HT, TH, TT.
If P(A) = 0.5, P(B) = 0.4 and P(A ∩ B) = 0.2, what is P(A ∪ B)?~0.7~0.9~1.1~0.3~0.5 + 0.4 − 0.2 = 0.7.
For mutually exclusive events A and B, P(A ∩ B) = ____.~0~1~P(A)P(B)~P(A) + P(B)~They cannot occur together.
A die is rolled. What is the probability that the number is greater than 4?~1/3~1/2~1/6~2/3~5 and 6 give 2 out of 6.
What is P(A′)?~1 − P(A)~P(A) − 1~P(A)~1 + P(A)~The complement rule.
Two dice are thrown. What is the probability that the sum is 7?~1/6~1/12~1/9~7/36~6 outcomes out of 36.
"""),
# ---------------- CLASS 12 ----------------
(12, B, '', 1, 'Relations and Functions', '🔗', """
A relation is an equivalence relation if it is ____.~reflexive, symmetric and transitive~reflexive and symmetric only~symmetric and transitive only~one-one and onto~All three properties must hold.
Is f: ℝ → ℝ, f(x) = 2x + 3 bijective?~Yes~No, it is not one-one~No, it is not onto~No, it is neither~It is both one-one and onto.
How many functions are there from a set with 2 elements to a set with 3 elements?~9~6~8~5~Each of the 2 elements has 3 choices, so 3² = 9.
How many bijections are there from a 3-element set to itself?~6~3~9~27~3! = 6.
If f(x) = x + 1 and g(x) = x², what is (g ∘ f)(2)?~9~5~4~25~f(2) = 3, g(3) = 9.
Is f: ℝ → ℝ, f(x) = x² one-one?~No~Yes~Yes, but not onto~Only on positive numbers~f(2) = f(−2), so it is not one-one.
"""),
(12, B, '', 2, 'Inverse Trigonometric Functions', '🔁', """
What is the principal value of sin⁻¹(1/2)?~π/6~π/3~π/4~π/2~sin(π/6) = 1/2.
What is the range of the principal value of sin⁻¹ x?~[−π/2, π/2]~[0, π]~(0, π)~[−π, π]~This is the standard principal range.
What is cos⁻¹(−1/2)?~2π/3~π/3~π/6~5π/6~cos(2π/3) = −1/2.
What is tan⁻¹(1)?~π/4~π/3~π/2~0~tan(π/4) = 1.
sin⁻¹x + cos⁻¹x = ____ for x ∈ [−1, 1].~π/2~π~0~2π~This is a standard identity.
What is the domain of sin⁻¹ x?~[−1, 1]~ℝ~[0, 1]~(−∞, 1]~The input of sin⁻¹ must lie between −1 and 1.
"""),
(12, B, '', 3, 'Matrices', '🟦', """
What is the order of a matrix with 2 rows and 3 columns?~2 × 3~3 × 2~2 × 2~6~Order = rows × columns.
(AB)ᵀ = ____.~BᵀAᵀ~AᵀBᵀ~ABᵀ~AB~The transpose reverses the order.
A square matrix A is symmetric if ____.~Aᵀ = A~Aᵀ = −A~A² = A~A = I~This is the definition of symmetric.
If A is 2 × 3 and B is 3 × 4, what is the order of AB?~2 × 4~3 × 3~4 × 2~2 × 3~Inner dimensions match and outer ones remain.
The diagonal entries of a skew-symmetric matrix are ____.~0~1~equal~negative~aᵢᵢ = −aᵢᵢ gives aᵢᵢ = 0.
For the identity matrix I, AI = ____.~A~I~0~A²~I is the multiplicative identity.
"""),
(12, B, '', 4, 'Determinants', '🔲', """
What is the determinant of [[1, 2], [3, 4]]?~−2~2~10~−10~1 × 4 − 2 × 3 = −2.
If A is a 3 × 3 matrix, |2A| = ____.~8|A|~2|A|~6|A|~9|A|~|kA| = kⁿ|A| for an n × n matrix.
A matrix is singular if its determinant is ____.~0~1~−1~negative~Singular matrices have no inverse.
The area of a triangle with given vertices can be found using ____.~½ times the absolute value of a determinant~the sum of coordinates~a determinant without ½~the product of coordinates~Area = ½ |det|.
The inverse of A exists if and only if ____.~|A| ≠ 0~|A| = 0~A is symmetric~A is singular~A non-zero determinant means the matrix is invertible.
A · adj(A) = ____.~|A| I~I~A²~0~This is the key property of the adjoint.
"""),
(12, B, '', 5, 'Continuity and Differentiability', '〰️', """
A function f is continuous at x = a if ____.~lim f(x) as x → a equals f(a)~f(a) is undefined~the limit is infinite~f is not defined near a~This is the definition.
Is f(x) = |x| differentiable at x = 0?~No~Yes~Only from the right~Yes, with derivative 1~The graph has a sharp corner at 0.
What is d/dx (eˣ)?~eˣ~xeˣ⁻¹~1/x~e~The exponential function is its own derivative.
What is d/dx (log x)?~1/x~x~eˣ~log x / x~The derivative of ln x is 1/x.
What is d/dx sin(2x)?~2 cos 2x~cos 2x~−2 cos 2x~2 sin 2x~By the chain rule.
What is d/dx (tan x)?~sec²x~cot x~−cosec²x~sec x tan x~This is a standard derivative.
"""),
(12, B, '', 6, 'Application of Derivatives', '⛰️', """
Where is the critical point of f(x) = x² − 4x?~x = 2~x = 4~x = 0~x = −2~f′(x) = 2x − 4 = 0.
A circle's radius grows at 1 cm/s. How fast is its area changing when r = 5 cm?~10π cm²/s~5π cm²/s~25π cm²/s~π cm²/s~dA/dt = 2πr · dr/dt = 10π.
A function f is increasing when ____.~f′(x) > 0~f′(x) < 0~f′(x) = 0~f″(x) > 0 only~A positive derivative means the function rises.
What is the maximum value of f(x) = −x² + 4?~4~0~2~−4~The maximum occurs at x = 0.
What is the slope of the tangent to y = x² at x = 3?~6~9~3~2~dy/dx = 2x = 6.
If f′(c) = 0 and f″(c) < 0, then f has a ____ at c.~local maximum~local minimum~point of inflection only~discontinuity~This is the second derivative test.
"""),
(12, B, '', 7, 'Integrals', '∫', """
What is ∫ x² dx?~x³/3 + C~2x + C~x³ + C~x²/2 + C~Add 1 to the power and divide by the new power.
What is ∫ cos x dx?~sin x + C~−sin x + C~cos x + C~tan x + C~The derivative of sin x is cos x.
What is ∫ (1/x) dx?~ln|x| + C~1/x² + C~x + C~−1/x + C~This is a standard integral.
What is ∫ eˣ dx?~eˣ + C~eˣ⁺¹ + C~x eˣ + C~ln x + C~The exponential function is its own integral.
What is ∫₀¹ 2x dx?~1~2~0~1/2~[x²] from 0 to 1 is 1.
What is ∫ sec²x dx?~tan x + C~sec x + C~cot x + C~−tan x + C~The derivative of tan x is sec²x.
"""),
(12, B, '', 8, 'Application of Integrals', '📐', """
What is the area under y = x from x = 0 to x = 2?~2~4~1~3~∫₀² x dx = [x²/2] = 2.
What is the area bounded by y = x², the x-axis and x = 3 (from x = 0)?~9~27~3~18~∫₀³ x² dx = 27/3 = 9.
What is the area of the circle x² + y² = a²?~πa²~2πa~πa~a²~This is the standard result.
The area between two curves is ____.~∫ (upper curve − lower curve) dx~∫ (lower − upper) dx~sum of both integrals~product of both curves~Subtract the lower function from the upper one.
What is the area under y = 2x from x = 1 to x = 3?~8~4~9~6~[x²] from 1 to 3 = 9 − 1 = 8.
What is the area of the ellipse x²/a² + y²/b² = 1?~πab~πa²b²~π(a + b)~ab~This is the standard result.
"""),
(12, B, '', 9, 'Differential Equations', '🔄', """
What is the order of d²y/dx² + y = 0?~2~1~0~3~The highest derivative is the second.
What is the degree of dy/dx + y = 0?~1~2~0~Not defined~The highest derivative has power 1.
What is the general solution of dy/dx = 2x?~y = x² + C~y = 2 + C~y = 2x² + C~y = x + C~Integrate both sides.
How many arbitrary constants are in the general solution of a third-order differential equation?~3~1~2~4~The number of constants equals the order.
What is the integrating factor of dy/dx + Py = Q?~e^(∫P dx)~e^(∫Q dx)~P~∫P dx~This is the standard integrating factor.
What is the solution of dy/dx = y?~y = Ceˣ~y = x + C~y = Cx~y = ln x~Separate variables: dy/y = dx.
"""),
(12, B, '', 10, 'Vector Algebra', '➡️', """
What is the magnitude of the vector 3i + 4j?~5~7~25~1~√(9 + 16) = 5.
What is i · j?~0~1~k~−1~Perpendicular unit vectors have zero dot product.
What is a × a for any vector a?~0 (the zero vector)~|a|²~a~1~A vector is parallel to itself.
What is the unit vector along 3i + 4j?~(3i + 4j)/5~3i + 4j~(3i + 4j)/7~(3i + 4j)/25~Divide by the magnitude.
What is the dot product of (1, 2, 3) and (4, 5, 6)?~32~15~21~28~4 + 10 + 18 = 32.
Two non-zero vectors a and b are perpendicular if ____.~a · b = 0~a × b = 0~|a| = |b|~a = b~The dot product is zero.
"""),
(12, B, '', 11, 'Three Dimensional Geometry', '🧊', """
For direction cosines l, m, n, we have l² + m² + n² = ____.~1~0~2~3~This is the standard identity.
What are the direction ratios of the x-axis?~1, 0, 0~0, 1, 0~0, 0, 1~1, 1, 1~The x-axis points along the positive x direction.
Two lines with direction ratios (a₁, b₁, c₁) and (a₂, b₂, c₂) are perpendicular if ____.~a₁a₂ + b₁b₂ + c₁c₂ = 0~a₁a₂ = b₁b₂ = c₁c₂~a₁/a₂ = b₁/b₂ = c₁/c₂~a₁ + a₂ = 0~Their dot product is zero.
What are the direction cosines of the z-axis?~0, 0, 1~1, 0, 0~0, 1, 0~1, 1, 1~The z-axis makes 90°, 90° and 0° with the axes.
For the plane ax + by + cz + d = 0, the normal has direction ratios ____.~a, b, c~d, a, b~1, 1, 1~−a, b, d~The coefficients of x, y and z give the normal.
What is the distance of the plane 2x + 3y + 6z = 14 from the origin?~2~14~7~1~14/√(4 + 9 + 36) = 14/7 = 2.
"""),
(12, B, '', 12, 'Linear Programming', '📈', """
The function to be maximised or minimised in a linear programming problem is called the ____.~objective function~constraint~feasible region~slack variable~It is the quantity we want to optimise.
The feasible region is the set of points that ____.~satisfy all the constraints~satisfy at least one constraint~violate all constraints~lie on the axes~Every constraint must hold at each of its points.
Where does the optimal value of the objective function occur?~At a corner point of the feasible region~At the origin only~At the centre of the region~Outside the region~This is the corner point theorem.
The non-negativity constraints are ____.~x ≥ 0, y ≥ 0~x ≤ 0, y ≤ 0~x + y = 0~x = y~Variables cannot be negative.
For Z = 3x + 4y, the corner points are (0, 0), (2, 0) and (0, 3). What is the maximum value of Z?~12~6~0~18~Z values are 0, 6 and 12.
A bounded feasible region ____.~has both a maximum and a minimum~has no maximum~has no minimum~is always empty~A linear function over a bounded region attains both extremes.
"""),
(12, B, '', 13, 'Probability', '🎯', """
P(A | B) = ____.~P(A ∩ B) / P(B)~P(A) / P(B)~P(A) × P(B)~P(B) / P(A ∩ B)~This is the formula for conditional probability.
Events A and B are independent if ____.~P(A ∩ B) = P(A) × P(B)~P(A ∩ B) = 0~P(A) = P(B)~P(A) + P(B) = 1~This is the definition of independence.
Which theorem finds the probability of a cause given an observed effect?~Bayes' theorem~Pythagoras' theorem~Binomial theorem~Rolle's theorem~Bayes' theorem reverses conditional probabilities.
If P(A) = 0.3 and P(B) = 0.4 are independent, what is P(A ∩ B)?~0.12~0.7~0.1~0.34~0.3 × 0.4 = 0.12.
Bernoulli trials have ____.~exactly two outcomes and are independent~three or more outcomes~dependent trials~no fixed number of outcomes~Each trial is success or failure, independent of the others.
What is the mean of a binomial distribution with n = 10 and p = 0.5?~5~10~2.5~0.5~Mean = np = 5.
"""),
]
