function [maxRows maxColumns] = GenerateSiftDescriptors( imageFileList, imageBaseDir, dataBaseDir, maxImageSize, gridSpacing, patchSize, canSkip )
%function [] = GenerateSiftDescriptors( imageFileList, imageBaseDir, dataBaseDir, maxImageSize, gridSpacing, patchSize, canSkip )
%
%Generate the dense grid of sift descriptors for each
% image
%
% imageFileList: cell of file paths
% imageBaseDir: the base directory for the image files
% dataBaseDir: the base directory for the data files that are generated
%  by the algorithm. If this dir is the same as imageBaseDir the files
%  will be generated in the same location as the image files
% maxImageSize: the max image size. If the image is larger it will be
%  resampeled.
% gridSpacing: the spacing for the grid to be used when generating the
%  sift descriptors
% patchSize: the patch size used for generating the sift descriptor
% canSkip: if true the calculation will be skipped if the appropriate data 
%  file is found in dataBaseDir. This is very useful if you just want to
%  update some of the data or if you've added new images.

fprintf('Building Sift Descriptors\n\n');

%% parameters

if(nargin<4)
    maxImageSize = 1000
end

if(nargin<5)
    gridSpacing = 8
end

if(nargin<6)
    patchSize = 16
end

if(nargin<7)
    canSkip = 0
end

maxColumns = 0;
maxRows = 0;

for f = 1:size(imageFileList,1)

    %% load image
    imageFName = imageFileList{f};
    [dirN base] = fileparts(imageFName);
    baseFName = [dirN filesep base];
    outFName = fullfile(dataBaseDir, sprintf('%s_dct.mat', baseFName));
    imageFName = fullfile(imageBaseDir, imageFName);
    
    if(size(dir(outFName),1)~=0 && canSkip)
        fprintf('Skipping %s\n', imageFName);
        continue;
    end
    
    [hgt,wid,x,y,siftArr,rows,columns] = getBlocks(imageFName,8,4);
    
    features.data = siftArr;
    features.x = x; %gridX(:) + patchSize/2 - 0.5;
    features.y = y; %gridY(:) + patchSize/2 - 0.5;
    features.wid = wid;
    features.hgt = hgt;

    sp_make_dir(outFName);
    save(outFName, 'features');
    
    %Calculate the maximum number of columns of the traspose of the data
    %array
    if (rows > maxColumns)
        maxColumns = rows;
    end
    maxRows = maxRows + columns;
    
end % for

end % function
