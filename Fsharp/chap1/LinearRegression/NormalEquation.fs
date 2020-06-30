module NormalEquation
open MathNet.Numerics.LinearAlgebra

let makedata (N:int) = 
    let X = DenseMatrix.init N 3 (fun i j -> if j = 0 then 1.0 else lib.randn())
    let beta = vector  [1.0; 2.0; 3.0]
    let noise = Vector<double>.Build.Random(N)

    let y = X * beta + noise

    X, y

let lsm (X:Matrix<double>, y:Vector<double>) =
    let beta = (X.Transpose() * X).Inverse() * (X.Transpose() * y)

    beta
    