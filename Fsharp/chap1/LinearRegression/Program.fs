module Program

let path = @"C:\home\myproj\StatisticalMLwith100\Fsharp\chap1\LinearRegression\fig\"
let N = 100

let LRrun = false
let NErun = false
let C2run = false
let STrun = false


[<EntryPoint>]
let main argv = 
    // 1.1 線形回帰
    if LRrun then
        let xs, ys = LR.makeData N
        let a, b = LR.min_sq(xs, ys)
        LR.plot_data(xs, ys, a, b, path) |> ignore
        printf "a = %A, b = %A\n" a b

    if NErun then
        let X, y = NormalEquation.makedata N
        let beta_hat = NormalEquation.lsm(X, y)

        printf "beta = %A\n" beta_hat

    if C2run then
        chisquares.plot_chi2(path) |> ignore
        printf "chi2"

    if STrun then
        student_t.plot_student_t(path) |> ignore
        printf "t"

    let xs, ys = Confidence.makeData N
    let p = 1

    let beta_hat, U = Confidence.fit(xs, ys)
    let RSE = Confidence.RSE(xs, ys, beta_hat, N, p)
    Confidence.plot(path, beta_hat, U, 0.95, RSE, N, p) |> ignore
    

    0 // return an integer exit code


