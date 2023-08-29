clc
clear all

% Define system
Rey = 400.0;
T = 200;
L = [-1.0/Rey 0; 1 -3.0/Rey];
% Exact solution using the norm function
% R_exact ¼ (norm(inv(ÿL)))ˆ2
% Define tolerance and initialize iterations
% tol ¼ 10ˆ(ÿ8);
% g = [rand; rand]; % (random initial guess)
% g = g/norm(g); % (normalize)
g = [0.63127; 0.77556];
% J = 10ˆ23; dJrel = 10ˆ23; it = 0;
% Iteration loop
% while (dJrel > tol)
% it ¼ it þ 1; Jold ¼ J;
Pdir = expm(T*L); % (solve state equation)
qT = Pdir*g;