class Solution():
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = min(strs, key=len)
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
    
## Koodi O notation - Memory
## O(1), sest et me loeme vaid mälluesimesi tähti ja võrdleme neid omavhael. 
## Ei kirjuta seda kuhugi mujale, vaid kasutame vaid võrdlemiseks mälu, see on konstantne 
## Koodi O notation - Time
## Peaks olema O(n*u), sest et me n = listi pikkus, u = listi tähtede arv, 
## sest me peame kõik elemendid läbi käima eesliidete kontrollimiseks ning see sõltub listi pikkusest ning tähtede arvust mõlemast