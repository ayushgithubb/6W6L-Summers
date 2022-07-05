ASSIGNMENT 2::::AYUSH GAUTAM ::::  200243
============================================================================

BOTH VECTORS ARE OF TYPE ANY.
TO ASSIGN VALUES TO THE VECTORS, WE TAKE A VARIABLE AND STORE IT WITH A
RANDOM VALUE::[0 TO 1)
NOW WE HAVE CONVERTED THE VALUE OF THIS VARIABLE IN A MANNER SO THAT IT LIES
BETWEEN THE GIVEN RANGE 1 TO 100.

NOW WE TRAVERSE THROUGH THE VECTORS AND USE THIS CONDITION TO ENSURE THAT THE RATIO OF
INTEGER AND FLOAT VALUES IS NEARLY 1:1 ::
IF VALUE RETURNED BY RANDOM < 0.5 WE ASSIGN A FLOAT VALUE TO VECTOR
OTHERWISE WE ASSIGN AN INTEGER VALUE.

 NOW IN  Solve1(V1,V2): WE HAVE CALCULATED THE REQUIRED SUM BY INITIALISING VARAIBLE
sum=0 SO IT IS OF ABSTRACT TYPE Union{Int64,Float64}.

IN Solve2(V1,V2): WE HAVE SET sum ALREADY TO Float64.


USING @code_warntype we can check type-stability of our functions.

Also using @time we see that timw taken by Solve2(V1,V2) is lesser.
Given below are the outputs returned by it.
============================================================================ 
OUTPUT IN TERMINAL::


f (generic function with 1 method)

Solve1 (generic function with 1 method)

Solve2 (generic function with 1 method)

julia> V1
10000-element Vector{Any}:
  10
  13.54077720893676
  88
  11.689424003615144
  25.788130050978097
   3
  98
  75
   8
   ⋮
  25.93958191165505
  39.97832824187327
  49
 100
  17.901702563549073
  28.28706120811233
  24.75465640304806
  47

julia> V2
10000-element Vector{Any}:
  5.347873976972306
 54
 39.705893454541716
 29.606172745522308
 72
 99
 20
 10.36116154293204
 20.82421527164121
  ⋮
 35.328662357612984
 14.072184519151676
 66
 49.301450157606475
 93
 88
  5.55168606182459
 91

julia> Solve1(V1,V2)
4.9585746583806226e11

julia> Solve2(V1,V2)
4.9585746583806226e11


julia> @code_warntype Solve1(V1,V2)

MethodInstance for Solve1(::Vector{Any}, ::Vector{Any})
  from Solve1(V1, V2) in Main at c:\Users\ayush\OneDrive\Documents\Assignment 2\Assignment2.jl:51
Arguments
  #self#::Core.Const(Solve1)
  V1::Vector{Any}
  V2::Vector{Any}
Locals
  @_4::Union{Nothing, Tuple{Int64, Int64}}
  sum::Any
  i::Int64
  y::Any
  x::Any
Body::Any
1 ─       (sum = 0)
│   %2  = (1:10000)::Core.Const(1:10000)
│         (@_4 = Base.iterate(%2))
│   %4  = (@_4::Core.Const((1, 1)) === nothing)::Core.Const(false)
│   %5  = Base.not_int(%4)::Core.Const(true)
└──       goto #4 if not %5
2 ┄ %7  = @_4::Tuple{Int64, Int64}
│         (i = Core.getfield(%7, 1))
│   %9  = Core.getfield(%7, 2)::Int64
│         (x = Base.getindex(V1, i))
│         (y = Base.getindex(V2, i))
│   %12 = sum::Any
│   %13 = Main.f(x, y)::Any
│         (sum = %12 + %13)
│         (@_4 = Base.iterate(%2, %9))
│   %16 = (@_4 === nothing)::Bool
│   %17 = Base.not_int(%16)::Bool
└──       goto #4 if not %17
3 ─       goto #2
4 ┄       return sum


julia> @code_warntype Solve1(V1,V2)
MethodInstance for Solve1(::Vector{Any}, ::Vector{Any})
  from Solve1(V1, V2) in Main at c:\Users\ayush\OneDrive\Documents\Assignment 2\Assignment2.jl:52
Arguments
  #self#::Core.Const(Solve1)
  V1::Vector{Any}
  V2::Vector{Any}
Locals
  @_4::Union{Nothing, Tuple{Int64, Int64}}
  sum::Any
  i::Int64
  y::Any
  x::Any
Body::Any
1 ─       (sum = 0)
│   %2  = (1:10000)::Core.Const(1:10000)
│         (@_4 = Base.iterate(%2))
│   %4  = (@_4::Core.Const((1, 1)) === nothing)::Core.Const(false)
│   %5  = Base.not_int(%4)::Core.Const(true)
└──       goto #4 if not %5
2 ┄ %7  = @_4::Tuple{Int64, Int64}
│         (i = Core.getfield(%7, 1))
│   %9  = Core.getfield(%7, 2)::Int64
│         (x = Base.getindex(V1, i))
│         (y = Base.getindex(V2, i))
│   %12 = sum::Any
│   %13 = Main.f(x, y)::Any
│         (sum = %12 + %13)
│         (@_4 = Base.iterate(%2, %9))
│   %16 = (@_4 === nothing)::Bool
│   %17 = Base.not_int(%16)::Bool
└──       goto #4 if not %17
3 ─       goto #2
4 ┄       return sum


julia> @code_warntype Solve2(V1,V2)
MethodInstance for Solve2(::Vector{Any}, ::Vector{Any})
  from Solve2(V1, V2) in Main at c:\Users\ayush\OneDrive\Documents\Assignment 2\Assignment2.jl:65
Arguments
  #self#::Core.Const(Solve2)
  V1::Vector{Any}
  V2::Vector{Any}
Locals
  @_4::Union{Nothing, Tuple{Int64, Int64}}
  sum::Float64
  i::Int64
  y::Any
  x::Any
Body::Float64
1 ─ %1  = Base.convert(Main.Float64, 0.0)::Core.Const(0.0)
│         (sum = Core.typeassert(%1, Main.Float64))
│   %3  = (1:10000)::Core.Const(1:10000)
│         (@_4 = Base.iterate(%3))
│   %5  = (@_4::Core.Const((1, 1)) === nothing)::Core.Const(false)
│   %6  = Base.not_int(%5)::Core.Const(true)
└──       goto #4 if not %6
2 ┄ %8  = @_4::Tuple{Int64, Int64}
│         (i = Core.getfield(%8, 1))
│   %10 = Core.getfield(%8, 2)::Int64
│         (x = Base.getindex(V1, i))
│         (y = Base.getindex(V2, i))
│   %13 = sum::Float64
│   %14 = Main.f(x, y)::Any
│   %15 = (%13 + %14)::Any
│   %16 = Base.convert(Main.Float64, %15)::Any
│         (sum = Core.typeassert(%16, Main.Float64))
│         (@_4 = Base.iterate(%3, %10))
│   %19 = (@_4 === nothing)::Bool
│   %20 = Base.not_int(%19)::Bool
└──       goto #4 if not %20
3 ─       goto #2
4 ┄       return sum


julia> @time Solve1(V1,V2)
  0.003162 seconds (19.99 k allocations: 312.344 KiB)
4.9585746583806226e11

julia> @time Solve2(V1,V2)
  0.003061 seconds (29.99 k allocations: 468.609 KiB)
4.9585746583806226e11
