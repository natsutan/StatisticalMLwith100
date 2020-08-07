module discriminant_analysis

type GaussDistri = 
    { cx :float
      cy :float
      sigma_1 :float
      sigma_2 :float
      rho: float
      }


let createGD(x:float, y:float,  s1:float,  s2:float,  rho:float ) : GaussDistri =
    {cx = x; cy = y; sigma_1 = s1; sigma_2 = s2; rho = rho}
    


