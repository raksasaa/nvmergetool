# nvmergetool
Tools to merge NV file

A NV file is a xml-as file
it might be like this:

```XML
<BURN>
<NV_ID="36">0,0,0,0</>
</BURN>

<NV_ID="1">0,0,0,1</>
<NV_ID="2">0,0,0,1,0,0,1</>
<NV_ID="4">0,0,0,1</>
<NV_ID="5">0,0,0,1</>
<NV_ID="6">7,0,0,1,0,0,1</>
<NV_ID="9">7,0,0,1,0,0,1</>
<NV_ID="53806">0,0,0,0</>

<NV_ID="1001">0,0,0,1</>
<NV_ID="1002">0,0,0,1,0,0,1</>
<NV_ID="1004">0,0,0,1</>
<NV_ID="1005">0,0,0,1</>
<NV_ID="1006">7,0,0,1,0,0,1</>
<NV_ID="1009">7,0,0,1,0,0,1</>
```
===
my workmate send me new nv data to merge

new nv data always like this:

```XML

<PS>
<NV_ID="3">0,0,0,1</>
<NV_ID="7">7,0,0,1,0,0,1</>
<NV_ID="8">7,0,0,1,0,0,1</>
</>

<RF>
<NV_ID="1003">1,1,1,1</>
<NV_ID="1004">1,1,0,1</>
</>
```
