%Construct a window in the shape of a semi-circle over a square, shown in the 2
%Figure. If the maximum allowable area of the window is 26 feet , 
%what dimension will result in the rectangle having largest possible area?

clc, clear all, close all

fitfunc = @area;
[x, fval] = ga(fitfunc,1,0,0);
disp(x)
% disp(fval)
fplot(fitfunc, [-50 50]);