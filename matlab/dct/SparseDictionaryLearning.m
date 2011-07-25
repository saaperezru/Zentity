
function [ ] = SparseDictionaryLearning( dataBaseDir, dictionarySize, canSkip )

%% Check if the file already exist
outFName = fullfile(dataBaseDir, sprintf('sparseDict_%d.mat', dictionarySize));
if(size(dir(outFName),1)~=0 && canSkip)
    fprintf('Dictionary file %s already exists.\n', outFName);
    return;
end

%% Load training patches
load('data/train_patches.mat');

%% Sparse dictionary learning
param.K = dictionarySize;
param.lambda = 0.15;
param.numThreads = 4; % number of threads
param.iter = 100;  % let us see what happens after 100 iterations.
tic
dictionary = mexTrainDL(sift_all',param)';
t=toc;
fprintf('time of computation for Dictionary Learning: %f\n',t);

%% Save the dictionary
fprintf('Saving texton dictionary\n');
sp_make_dir(outFName);
save(outFName, 'dictionary');