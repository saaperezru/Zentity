function [Wt Ft Wv Fv Hv Tt imgIdsTraining Iv XvTraining XtTraining]=nmf_clustering_multimodal_asymmetric (path, r, type,beginFrom)

visual = importdata(strcat(path, '/features/visual/visual.txt'));
XvTraining = visual.data;
imgIdsTraining = visual.textdata(:,1);

clear visual;

XtTraining = load(strcat(path, '/features/text/index_',type,'.txt'));
XtTraining = full(spconvert(XtTraining));

terms = importdata(strcat(path, '/features/text/tokens_',type,'.txt'));
terms = terms.textdata;


% To avoid zeros in the factorization
XtTraining = XtTraining + 1e-10;
XvTraining = XvTraining + 1e-10;

% Normalization

XtTraining = XtTraining';
XvTraining = XvTraining';
XtTraining = normalize(XtTraining',1);
XvTraining = normalize(XvTraining',1);
XtTraining = XtTraining';
XvTraining = XvTraining';

disp('Features loaded...');
    
disp(strcat('r=', num2str(r)));
if (beginFrom == 'textual')
	%Initialize with kmeans
	[IDX C] = kmeans(XtTraining', r, 'emptyaction','singleton');

	H = zeros(r, size(XtTraining,2));

	for i =1:r 
		H(i, find(IDX==i)) = 1; 
	end

	H0 = H + 0.2*(ones(size(H)));
	W0 = H0'*(diag(sum(H,2)))^-1;

	% Finding Ht for Xt

	[Wt Ht] = nmf_convex_2(XtTraining, r, 'W0', W0, 'H0', H0);
	Ft = XtTraining*Wt;


	disp('Symmetric step ended...');

	% Asymmetric step
	[Wv Hv] = nmf_convex_2(XvTraining, r, 'verb', 2, 'H', Ht);
	Fv = XvTraining*Wv;

	disp('Asymmetric step ended...');
elseif(beginFrom=='visual')
	%Initialize with kmeans
	[IDX C] = kmeans(XvTraining', r, 'emptyaction','singleton');

	H = zeros(r, size(XvTraining,2));

	for i =1:r 
		H(i, find(IDX==i)) = 1; 
	end

	H0 = H + 0.2*(ones(size(H)));
	W0 = H0'*(diag(sum(H,2)))^-1;

	% Finding Ht for Xt

	[Wv Hv] = nmf_convex_2(XvTraining, r, 'W0', W0, 'H0', H0);
	Fv = XvTraining*Wv;


	disp('Symmetric step ended...');

	% Asymmetric step
	[Wt Ht] = nmf_convex_2(XtTraining, r, 'verb', 2, 'H', Hv);
	Ft = XtTraining*Wt;

	disp('Asymmetric step ended...');	
end
%Generating ordered list of terms
[Bs IXTt] = sort(Ft,'descend');

Tt = terms(IXTt(:,:));


% Matrix with image clusters (multimodal summarization)
[Cv IXDv] = sort(Wv,'descend');
Iv = imgIdsTraining(IXDv(:,:));


disp('Images in each cluster:');
sum(Hv')