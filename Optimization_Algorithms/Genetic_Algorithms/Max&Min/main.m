%Find the maximum and minimum of x5 - 6x3 + 4x + 2 between -2, 2 using genetic algorithms.

clc, clear all, close all

fitfunc = @myFunc;
% fplot(fitfunc,[-2 2]);
[x, fval] = ga(fitfunc,1,-0,0);   %Finding the max
%[x,fval] = ga(fitfunc,1,-2,2);	  %Finding the min

% disp(vpa(x,4)); %min x value
disp(vpa(fval,4)); %min y value
fplot(@myFunc,[-2.5 2.5])