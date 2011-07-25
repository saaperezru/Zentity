function main(path,datasetName,url,r,iter,type,beginFrom,concepts,images)

	errorMin = Inf();
	minMatrix = -1;
	for i =1:iter
		[Wt Ft Wv Fv H Tt imgIdsTraining Iv XvTraining XtTraining] = nmf_clustering_multimodal_asymmetric(path,r,type,beginFrom);
		H_norm = normalize(H',1); 
		save(strcat(path,'/data/',beginFrom,'/','Hv_iter_', int2str(i), '.mat'), 'H');	      
		save(strcat(path,'/data/',beginFrom,'/','H_iter_',  int2str(i), '.mat'), 'H_norm');
		save(strcat(path,'/data/',beginFrom,'/','Wv_iter_', int2str(i), '.mat'), 'Wv');
		save(strcat(path,'/data/',beginFrom,'/','Wt_iter_', int2str(i), '.mat'), 'Wt');
		save(strcat(path,'/data/',beginFrom,'/','Ft_iter_', int2str(i), '.mat'), 'Ft');
		save(strcat(path,'/data/',beginFrom,'/','Fv_iter_', int2str(i), '.mat'), 'Fv');
		save(strcat(path,'/data/',beginFrom,'/','Tt_iter_', int2str(i), '.mat'), 'Tt');
		save(strcat(path,'/data/',beginFrom,'/','Iv_iter_', int2str(i), '.mat'), 'Iv');
		save(strcat(path,'/data/',beginFrom,'/','imgIds_iter_', int2str(i), '.mat'), 'imgIdsTraining');
		% Extract most important latent topics for each image
		[TMP indexSortedLT] =  sort(H,'descend');
		indexSortedLT = indexSortedLT(1,:);
		save(strcat(path,'/data/',beginFrom,'/','SortedLT_iter_', int2str(i), '.mat'),'indexSortedLT');
		%Saving the diference of the visual matrix
		FH = Fv*H;
		diff = XvTraining - FH;
		error = norm(diff, 'fro'); 
		%Saving the error of the textual matrix
		FH = Ft*H;
		diff = XtTraining - FH;
		error = error + norm(diff, 'fro');
		
		disp(strcat('Error for iteration ', num2str(i), '  was  ', num2str(error)))
		
		if (error<errorMin)
			errorMin=error;
			minMatrix=i;
		end
		clear Wt;
		clear Ft;
		clear Wv;
		clear Fv;
		clear Hv;
		clear Tt;
		clear imgIdsTraining;
		clear Iv;
		clear TMP;
		clear H_norm;
		clear indexSortedLT;
	end
	
	for i=1:iter
		if (i~=minMatrix)
			delete(strcat(path,'/data/',beginFrom,'/','Hv_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','H_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','Wv_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','Wt_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','Ft_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','Fv_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','Tt_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','Iv_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','imgIds_iter_', int2str(i), '.mat'),strcat(path,'/data/',beginFrom,'/','SortedLT_iter_', int2str(i), '.mat'));
		end
	end

	file = load(strcat(path,'/data/',beginFrom,'/','Tt_iter_',num2str(minMatrix),'.mat'));
	Tt = file.Tt;
	
	file = load(strcat(path,'/data/',beginFrom,'/','Iv_iter_',num2str(minMatrix),'.mat'));
	Iv = file.Iv;

	file = load(strcat(path,'/data/',beginFrom,'/','imgIds_iter_',num2str(minMatrix),'.mat'));
	imgIdsTraining = file.imgIdsTraining;
	clear file;
	printClustersHTML(r, dataset, path, errorMin,beginFrom);
	printHTML(dataset, path, url, Tt, Iv, imgIdsTraining, concepts, images, r, beginFrom);
	
end
