% Example of how to use the BuildPyramid function
% set image_dir and data_dir to your actual directories

% FLICKR DATA
image_dir = '/Users/jorgecamargo/Documents/workspace/Flickr/images'; 
data_dir = '/Users/jorgecamargo/Documents/workspace/Flickr/data';

%image_dir = '/home/jccaicedo/corel5k/tmp/imgs';
%data_dir = '/home/jccaicedo/corel5k/tmp/data';


% for other parameters, see BuildPyramid

fnames = dir(fullfile(image_dir, '*.jpg'));
num_files = size(fnames,1);
filenames = cell(num_files,1);

for f = 1:num_files
	filenames{f} = fnames(f).name;
end

% return pyramid descriptors for all files in filenames
pyramid_all = BuildPyramid(filenames,image_dir,data_dir);
save -ASCII bagOfFeatures_dct1000_appleflickr_.txt pyramid_all;
save jc_tmp.mat filenames;

% build a pyramid with a different dictionary size without re-generating the
% sift descriptors.
%pyramid_all2 = BuildPyramid(filenames,image_dir,data_dir,1000,100,50,4,1);

% compute histogram intersection kernel
%K = hist_isect(pyramid_all, pyramid_all); 

% for faster performance, compile and use hist_isect_c:
% K = hist_isect_c(pyramid_all, pyramid_all);
