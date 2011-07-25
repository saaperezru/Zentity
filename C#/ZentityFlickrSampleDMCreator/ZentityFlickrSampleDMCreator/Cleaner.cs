using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zentity.Core;
using Zentity.Flickr.Sample2;
using System.Collections;


namespace ZentityFlickrSampleDMCreator
{
    class Cleaner
    {
        public void deleteALL(ZentityContext context)
        {
            ArrayList l = new ArrayList();
            foreach (ImageResource2 img in context.Resources.OfType<ImageResource2>())
            {
                foreach (Zentity.Core.File f in img.Files)
                {
                    context.DeleteResourceHasFile(img.Id, f.Id);
                    context.DeleteResourceHasFile(f.Id, img.Id);
                    
                    context.DeleteResource(f.Id);
                }
                l.Add(img.Id);
            }
            foreach (Guid g in l)
                context.DeleteResource(g);
        }
    }
}
