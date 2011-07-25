%% Sparse Experiments
% set image_dir and data_dir to your actual directories
image_dir = 'imagesCorel'; 
data_dir = 'data';

fnames = dir(fullfile(image_dir, '*.jpg'));
num_files = size(fnames,1);
filenames = cell(num_files,1);

for f = 1:num_files
	filenames{f} = fnames(f).name;
end

%% Process Data
dictionarySize = 1000;
canSkip = 1;
SparseDictionaryLearning( data_dir, dictionarySize, canSkip);
H_all = SparseHistograms( filenames, data_dir, '_sift.mat', dictionarySize, canSkip );
save -ASCII bagOfFeatures.txt H_all;
save jc_tmp.mat filenames;