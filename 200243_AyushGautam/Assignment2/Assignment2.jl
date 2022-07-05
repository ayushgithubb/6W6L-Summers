using BenchmarkTools

V1 = Vector{Any}(undef,10000)   ## vector of type "Any"

V2 = Vector{Any}(undef,10000)

for i = 1:10000
  ## filling V1
  x=rand()
  y=x
  while(true)
    if !(y>1&&y<100)      ## converting the value returned by rand() to lie in the range 1-100
      y*=100
    else
      break
    end
  end
  if x<0.5                ## if the random value returned is < 0.5 assign a float value(so that the ratio can be nearly 1:1)
    V1[i]=y  
  else
    V1[i]=rand((1:100))   ## otherwise assign an integer value between 1 and 100
  end
end


for i = 1:10000
  ## filling V2
  x=rand()
  y=x
  while(true)
    if !(y>1&&y<100)
      y*=100
    else
      break
    end
  end
  if x<0.5
    V2[i]=y
  else
    V2[i]=rand((1:100))
  end
end 

function f(x,y)    ## defining f(x,y) as per question
  if x>y
    return 4x^4+9x^2+10x+1
  else
    return y^4+3y^2+9y+2
  end
end

function Solve1(V1,V2)   
  sum=0           ## sum will have the abstract type Union{Int64,Float64 }
  for i = 1:10000
    x=V1[i]
    y=V2[i]
    sum+=f(x,y)

  end
  return sum

end


function Solve2(V1,V2)
  sum::Float64=0.0  ## defining the type of sum as Float64
  for i = 1:10000
    x=V1[i]
    y=V2[i]
    sum+=f(x,y)
  end
  return sum  
end
