module lib

// Learn more about F# at http://fsharp.org
// See the 'F# Tutorial' project for more help.
open MathNet.Numerics.Distributions


//Pythonのrandn
let randn():double = 
    Normal(mean=0.0, stddev=1.0).Sample()

