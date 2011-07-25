function [hgt,wid,x,y,patches] = getBlocks(image_fname,patchSize,gridSpacing)

maxImageSize = 256;
T = dctmtx(patchSize);

I = imread(image_fname);
I = im2double(I);

[hgt wid chn] = size(I);
if min(hgt,wid) > maxImageSize
    I = imresize(I, maxImageSize/min(hgt,wid), 'bicubic');
    [hgt wid chn] = size(I);
end

remX = mod(wid-patchSize,gridSpacing);
offsetX = floor(remX/2)+1;
remY = mod(hgt-patchSize,gridSpacing);
offsetY = floor(remY/2)+1;

[gridX,gridY] = meshgrid(offsetX:gridSpacing:wid-patchSize+1, offsetY:gridSpacing:hgt-patchSize+1);

fprintf('Processing %s: wid %d, hgt %d, grid size: %d x %d, %d patches\n', ...
        image_fname, wid, hgt, size(gridX,2), size(gridX,1), numel(gridX));

num_patches = numel(gridX);
vector_size = patchSize^2;
patches = zeros(vector_size*3, num_patches);
for k=1:num_patches
    x_lo = gridX(k);
    x_hi = gridX(k) + patchSize - 1;
    y_lo = gridY(k);
    y_hi = gridY(k) + patchSize - 1;

    patch = [];
    for channel=1:chn
        block = I(y_lo:y_hi,x_lo:x_hi,channel);
        coeff = T*block*T';
        tmp = sort(reshape(coeff,[1 vector_size]),'descend');
        coeff(coeff < tmp(21)) = 0;
        patch = [ patch; reshape(coeff,[vector_size 1]) ];
    end
    % Images with no color information: Copy the only channel to R, G and B
    if chn == 1
      patch = [patch; patch; patch];
    end

    patches(:,k) = patch;
    %patches(:,k) = patches(:,k)/norm(patches(:,k));
end

x = gridX(:) + patchSize/2 - 0.5;
y = gridY(:) + patchSize/2 - 0.5;
%patches = patches';

end
