function [Ft Tt IXTt Xs XtTraining Wt Ht XvTraining Wv]=nmf_clustering_flickr_multimodal_asymmetric ()

concepts=10;
images=10;

path = '/datos/doctorado/Exploration/Conferences/acmmm/acmm11/';

visual = importdata('visual.txt');
XvTraining = visual.data;
imgIdsTraining = visual.textdata(:,1);
%XvTraining = full(spconvert(visual));
%imgIdsTraining = load(strcat(path, '/features/', dataset,'/visual/idsQuery1-1000.txt'));

clear visual;
 
XtTraining = load('index.txt');
XtTraining = full(spconvert(XtTraining));
Xs = XtTraining;

terms = importdata('tokens.txt');
terms = terms.textdata;

url = strcat('/storageHP/jecamargom/flickr/colombia2/images/');
 
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

		 %[B I] = sort(Ft, 'descend');

		 [m n] = size(Ft);
		 Ft = Ft.*log(Ft./(repmat(prod(Ft'),n,1)'.^(1/r)));

				   [Vt Idxt] = sort(Ft, 'descend');

				   FtIdx = zeros(size(Ft));

				   for i = 1:20
				   for j = 1:20
				   FtIdx(Idxt(i,j),j) = 1;
    end
end

				   for j=1:837
				   if isempty(find(Idxt(1:20,:)==j)) 
				   Ft(j,:) = 0;
    end
end

				   Ft = Ft .* FtIdx;
				   [Bs IXTt] = sort(Ft,'descend');

				   Tt = terms(IXTt(:,:));


				   disp('Symmetric step ended...');

% Asymmetric step
				   [Wv Hv] = nmf_convex_2(XvTraining, r, 'verb', 2, 'H', Ht);
				   Fv = XvTraining*Wv;

				   disp('Asymmetric step ended...');


				   disp('Images in each cluster:');
				   sum(Hv')


[Cv IXDv] = sort(Wv,'descend');

% Matrix with image clusters (multimodal summarization)
Iv = imgIdsTraining(IXDv(:,:));

disp('Se acabo de ejecutar el script');

%printClustersHTML(r, dataset, path);
%printHTML(dataset, path, url, Tt, Iv, imgIdsTraining, concepts, images, r);
