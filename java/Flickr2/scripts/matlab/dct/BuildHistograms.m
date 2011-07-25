function [ H_all ] = BuildHistograms( imageFileList, dataBaseDir, featureSuffix, dictionarySize, canSkip )
%function [ H_all ] = BuildHistograms( imageFileList, dataBaseDir, featureSuffix, dictionarySize, canSkip )
%
%find texton labels of patches and compute texton histograms of all images
%   
% For each image the set of sift descriptors is loaded and then each
%  descriptor is labeled with its texton label. Then the global histogram
%  is calculated for the image. If you wish to just use the Bag of Features
%  image descriptor you can stop at this step, H_all is the histogram or
%  Bag of Features descriptor for all input images.
%
% imageFileList: cell of file paths
% imageBaseDir: the base directory for the image files
% dataBaseDir: the base directory for the data files that are generated
%  by the algorithm. If this dir is the same as imageBaseDir the files
%  will be generated in the same location as the image file
% featureSuffix: this is the suffix appended to the image file name to
%  denote the data file that contains the feature textons and coordinates. 
%  Its default value is '_sift.mat'.
% dictionarySize: size of descriptor dictionary (200 has been found to be
%  a good size)
% canSkip: if true the calculation will be skipped if the appropriate data 
%  file is found in dataBaseDir. This is very useful if you just want to
%  update some of the data or if you've added new images.

fprintf('Building Histograms\n\n');

%% parameters

if(nargin<3)
    dictionarySize = 200
end

if(nargin<4)
    canSkip = 0
end

%% load texton dictionary (all texton centers)

inFName = fullfile(dataBaseDir, sprintf('dictionary_dct_%d.mat', dictionarySize));
load(inFName,'dictionary');
fprintf('Loaded DCT dictionary: %d textons\n', dictionarySize);

%% compute texton labels of patches and whole-image histograms
H_all = [];

for f = 1:size(imageFileList,1)

    imageFName = imageFileList{f};
    [dirN base] = fileparts(imageFName);
    baseFName = fullfile(dirN, base);
    inFName = fullfile(dataBaseDir, sprintf('%s%s', baseFName, featureSuffix));
    
    outFName = fullfile(dataBaseDir, sprintf('%s_ind_%d.mat', baseFName, dictionarySize));
    outFName2 = fullfile(dataBaseDir, sprintf('%s_dct_hist_%d.mat', baseFName, dictionarySize));
    if(size(dir(outFName),1)~=0 && size(dir(outFName2),1)~=0 && canSkip)
        fprintf('Skipping %s\n', imageFName);
        load(outFName2, 'H');
        H_all = [H_all; H];
        continue;
    end
    
    %% load sift descriptors
    load(inFName, 'features');
    ndata = size(features.data,2);
    fprintf('Loaded %s, %d descriptors\n', inFName, ndata);

    %% find texton indices and compute histogram 
    texton_ind.data = zeros(ndata,1);
    texton_ind.x = features.x;
    texton_ind.y = features.y;
    texton_ind.wid = features.wid;
    texton_ind.hgt = features.hgt;
    %run in batches to keep the memory foot print small
    batchSize = 50000;
    if ndata <= batchSize
        %param.L = 50;
        %param.eps = 0.01;
        %dist_mat = mexOMP(features.data', dictionary', param);
        dist_mat = sp_dist2(features.data', dictionary);
        [min_dist, min_ind] = min(dist_mat, [], 2);
        texton_ind.data = min_ind;
    else
        for j = 1:batchSize:ndata
            lo = j;
            hi = min(j+batchSize-1,ndata);
            dist_mat = dist2(features.data(lo:hi,:), dictionary);
            %param.L = 50;
            %dist_mat = mexOMP(features.data(lo:hi),dictionary,param);
            [min_dist, min_ind] = min(dist_mat, [], 2);
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
outFName = fullfile(dataBaseDir, sprintf('histograms_dct_%d.mat', dictionarySize));
save(outFName, 'H_all', '-ascii');

end
