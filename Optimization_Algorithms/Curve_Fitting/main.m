clc, clear all, close all
days = (1:38);
cases = [777 823 887 1766 2988 4835 5374 7123 8459 11236 8789 13963 16797 18695 19979 18360 21595 24998 27103 28819 32425 34272 25398 30561 30613 33323 33901 35527 28391 27620 25023 26922 30148 31667 30833 32922 24601 28065];
passaway = [10 12 16 23 42 0 110 80 131 119 211 249 246 411 484 318 661 909 1059 915 1104 1344 1146 1342 1906 1922 1873 2087 1831 1500 1541 2408 4928 2299 3770 1856 1772 1857];

c = polyfit(days,cases,4);        %for cases
p = polyfit(days,passaway,3);     %for passaway

% x = 1:1:38;
x = 1:1:45;   %predicting the next 7 days

y1 = polyval(c,x,'extrap');
y2 = polyval(p,x,'extrap');

plot(days,cases,'o',x,y1)
hold on
plot(days,passaway,'*',x,y2)
xlabel('Days');
ylabel('Number of people');
title('functions for number of cases and passaways')
% title('functions for number of cases and passaways predicting 7 additional days')

grid on
s = sprintf('y =(%.1f) x^4 + (%.1f) x^3 + (%.1f) x^2 + (%.1f) x + (%.1f)',c(1),c(2),c(3),c(4),c(5));
p = sprintf('y = (%.1f) x^3 + (%.1f) x^2 + (%.1f) x + (%.1f)',p(1),p(2),p(3),p(4));


% text(2,30000,s);
% text(20,400,p);


