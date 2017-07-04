This text file introduces the structure of the scripts of 3-period OG model
There are 9 scripts in the folder:
1. 3period_OG_execution.py    : main execution script for both steady state and transitional state OG model
2. aggregatevar_func.py       : functions to derive capital and labor
3. price_func.py              : functions to derive wage and interest rate
4. consumption_func.py        : functions to derive consumption
5. utility_func.py            : functions to derive marginal utility
6. euler_func.py              : functions to derive errors of Euler equation
7. timepath_func.py           : functions to derive/update the time path of aggregate variables
8. HHsoltion_func.py          : function  to derive calculated time path based on given ones
9. TSconvergence_func.py      : function  to derive the converged transitional state equilibrium

After putting all of them into one folder, just run the main execution script: 3period_OG_execution.py

Structure of the scripts ("->" indicates the script on the lhs is the foundation of scripts on the rhs)
I. steady state equilibrium
   aggregatevar_func.py  ->  price_func.py  ->  consumption_func.py  ->   utility_func.py  ->  euler_func.py  ->  3period_OG_execution.py 

II. transitional state equilibrium
   
   euler_func.py  ->  HHsolution_func.py  ->  ]
                                              ] -> TSconvergence_func.py  ->   3period_OG_execution.py
                        timepath_func.py  ->  ]