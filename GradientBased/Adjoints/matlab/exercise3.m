% Define system
Rey = 40.0;
L = [-1.0/Rey 0; 1 -3.0/Rey];
% Exact solution using the norm function
% R_exact ¼ (norm(inv(ÿL)))ˆ2
% Define tolerance and initialize iterations
% tol ¼ 10ˆ(ÿ8);
% g = [rand; rand]; % (random initial guess)
% g = g/norm(g); % (normalize)
g = [0.63127; 0.77556]
% J = 10ˆ23; dJrel = 10ˆ23; it = 0;
% Iteration loop
% while (dJrel > tol)
% it ¼ it þ 1; Jold ¼ J;
q = -inv(L)*g; % (solve state equation)
g2 = g'*g; q2 = q'*q;
J = g2/q2; % (objective function)
R = 1.0/J;
% dJrel ¼ abs((J – Jold)/J);
a = -2*(inv(L')*q)*(g2)/q2^2;%(solve adjoint equation)
g = a*q2/2.0; % (enforce optimality eq.)
g = g/norm(g); % (normalize)
% end % (end of iteration loop)
% % optimal amplification

% % print results
% it, R % (final iteration and amplification)
% g % (optimal forcing (defined up to a constant)
% q % (optimal response)