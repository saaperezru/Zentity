function main(path,datasetName,url,r,iter,type,beginFrom,concepts,images)


	minMatrix = 4;
	errorMin = 0;

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
