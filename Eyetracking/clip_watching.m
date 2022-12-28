%http://antoinecoutrot.magix.net/public/databases.html
DBItem = fullfile(GitHubRoot, 'EyeTracking', 'coutrot_database2.mat');
loadvars = load(DBItem);
Coutrot_Database2 = loadvars.Coutrot_Database2;
C = Coutrot_Database2.Visual;
clips = fieldnames(C);

currClip = C.(clips{1}).data;
info = C.(clips{1}).info;

screen = nan(info.vidwidth, info.vidheight);


figure(1);
clf;
hold on
for ix = 1:size(currClip,3) % loop across participants
    pos = [(squeeze(currClip(1,:,ix)))', (squeeze(currClip(2,:,ix)))'];
    if isempty(pos)
        continue
    end
    scatter(pos(:,1), pos(:,2), 20);
%     plot(pos(:,1), pos(:,2), '--');
%     pause(0.1);
end
legend




%%