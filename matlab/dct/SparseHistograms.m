function [ H_all ] = SparseHistograms( imageFileList, dataBaseDir, featureSuffix, dictionarySize, canSkip )

fprintf('Building Histograms\n\n');

%% parameters

if(nargin<3)
    dictionarySize = 200
end

if(nargin<4)
    canSkip = 0
end

%% load texton dictionary (all texton centers)

inFName = fullfile(dataBaseDir, sprintf('sparseDict_%d.mat', dictionarySize));
load(inFName,'dictionary');
fprintf('Loaded texton dictionary: %d textons\n', dictionarySize);

%% compute texton labels of patches and whole-image histograms
H_all = [];

for f = 1:size(imageFileList,1)

    imageFName = imageFileList{f};
    [dirN base] = fileparts(imageFName);
    baseFName = fullfile(dirN, base);
    inFName = fullfile(dataBaseDir, sprintf('%s%s', baseFName, featureSuffix));
    
    outFName = fullfile(dataBaseDir, sprintf('%s_texton_ind_%d.mat', baseFName, dictionarySize));
    outFName2 = fullfile(dataBaseDir, sprintf('%s_hist_%d.mat', baseFName, dictionarySize));
    if(size(dir(outFName),1)~=0 && size(dir(outFName2),1)~=0 && canSkip)
        fprintf('Skipping %s\n', imageFName);
        load(outFName2, 'H');
        H_all = [H_all; H];
        continue;
    end
    
    %% load sift descriptors
    load(inFName, 'features');
    ndata = size(features.data,1);
    fprintf('Loaded %s, %d descriptors\n', inFName, ndata);

    %% find texton indices and compute histogram 
    texton_ind.data = zeros(ndata,1);
    texton_ind.x = features.x;
    texton_ind.y = features.y;
    texton_ind.wid = features.wid;
    texton_ind.hgt = features.hgt;
    %run in batches to keep the memory foot print small
    batchSize = 10000;
    if ndata <= batchSize
        param.L = 50;
        param.eps = 0.01;
        dist_mat = mexOMP(features.data', dictionary', param);
        [min_dist, min_ind] = max(dist_mat, [], 2);
        texton_ind.data = min_ind;
    else
        for j = 1:batchSize:ndata
            lo = j;
            hi = min(j+batchSize-1,ndata);
            param.L = 50;
            dist_mat = mexOMP(features.data(lo:hi),dictionary,param);
            [min_dist, min_ind] = max(dist_mat, [], 2);
            texton_ind.data(lo:hi,:) = min_ind;
        end
    end

    H = hist(texton_ind.data, 1:dictionarySize);
    H_all = [H_all; H];

    %% save texton indices and histograms
    save(outFName, 'texton_ind');
    save(outFName2, 'H');
end

%% save histograms of all images in this directory in a single file
outFName = fullfile(dataBaseDir, sprintf('histograms_%d.mat', dictionarySize));
save(outFName, 'H_all', '-ascii');


end
