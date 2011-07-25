function main(path,datasetName,url,r,iter,type,beginFrom,concepts,images)

	errorMin = Inf();
	min = -1;
	for i =1:iter
		[Wt Ft Wv Fv H Tt imgIdsTraining Iv XvTraining XtTraining] = nmf_clustering_multimodal_asymmetric(path,r,type,beginFrom);
		H_norm = normalize(H',1); 
		save(strcat(path,'/data/','Hv_iter_', int2str(i), '.mat'), 'H');	      
		save(strcat(path,'/data/','H_iter_',  int2str(i), '.mat'), 'H_norm');
		save(strcat(path,'/data/','Wv_iter_', int2str(i), '.mat'), 'Wv');
		save(strcat(path,'/data/','Wt_iter_', int2str(i), '.mat'), 'Wt');
		save(strcat(path,'/data/','Ft_iter_', int2str(i), '.mat'), 'Ft');
		save(strcat(path,'/data/','Fv_iter_', int2str(i), '.mat'), 'Fv');
		save(strcat(path,'/data/','Tt_iter_', int2str(i), '.mat'), 'Tt');
		save(strcat(path,'/data/','Iv_iter_', int2str(i), '.mat'), 'Iv');
		save(strcat(path,'/data/','imgIds_iter_', int2str(i), '.mat'), 'imgIdsTraining');
		% Extract most important latent topics for each image
		[TMP indexSortedLT] =  sort(H,'descend');
		indexSortedLT = indexSortedLT(1,:);
		save(strcat(path,'/data/','SortedLT_', int2str(i), '.mat'),'indexSortedLT');
		%Saving the diference of the visual matrix
		FH = Fv*H;
		diff = XvTraining - FH;
		error = norm(diff, 'fro'); 
		%Saving the error of the textual matrix
		FH = Ft*H;
		diff = XtTraining - FH;
		error = error + norm(diff, 'fro');
		
		disp(strcat('Error for iteration ', num2str(i), ' was ', num2str(error)))
		
		if (error<errorMin)
			errorMin=error;
			min=i;
			fTt = Tt;
			fIv = Iv;
			fImgIdsTraining = ImgIdsTraining;
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
		if (i~=min)
			delete(strcat(path,'/data/','Hv_iter_', int2str(i), '.mat'),strcat(path,'/data/','H_iter_', int2str(i), '.mat'),strcat(path,'/data/','Wv_iter_', int2str(i), '.mat'),strcat(path,'/data/','Wt_iter_', int2str(i), '.mat'),strcat(path,'/data/','Ft_iter_', int2str(i), '.mat'),strcat(path,'/data/','Fv_iter_', int2str(i), '.mat'),strcat(path,'/data/','Tt_iter_', int2str(i), '.mat'),strcat(path,'/data/','Iv_iter_', int2str(i), '.mat'),strcat(path,'/data/','imgIds_iter_', int2str(i), '.mat'));
		end
	end
	
	
	printClustersHTML(r, dataset, path, errorMin);
	printHTML(dataset, path, url, fTt, fIv, fImgIdsTraining, concepts, images, r);
	
end