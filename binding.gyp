	{
	'targets': [{
		'target_name': 'addon',
		'sources': [ 
			'src/addon.cpp',
			'src/opencv_manual.cpp', 
			'src/opencvjs.cpp'
		],
		'cflags' : ['-Wno-unused-variable'],
		'cflags!': [ '-fno-exceptions'],
		'cflags_cc!': [ '-fno-exceptions'],
		'conditions': [
			[ 'OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"',{
				'ldflags': [ '<!@(pkg-config --libs --libs-only-other opencv)' ],
				'libraries': [ '<!@(pkg-config --libs opencv)' ],
				'cflags': [ '<!@(pkg-config --cflags opencv)' ],
				'cflags_cc': [ '<!@(pkg-config --cflags opencv)' ],
				'cflags_cc!': ['-fno-rtti'],
				'cflags_cc+': ['-frtti']
			}],
	        ['OS=="mac"', {
	        	'include_dirs':['/usr/local/include/opencv'],
	          'xcode_settings': {
	            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
	          },
	          'libraries':[
							'-lopencv_core', 
							'-lopencv_imgproc', 
							'-lopencv_calib3d',
							'-lopencv_features2d', 
							'-lopencv_objdetect', 
							'-lopencv_video', 
							'-lopencv_highgui', 
							'-lopencv_contrib', 
							'-lopencv_flann', 
							'-lopencv_ml', 
							'-lopencv_gpu', 
							'-lopencv_legacy'
	          ]
	        }],

	        ['OS=="win"', 
	        	{
		        	'include_dirs':['$(OPENCV_ROOT)/build/include', '$(OPENCV_ROOT)/build/include/opencv'],
		        	'library_dirs':['$(OPENCV_ROOT)/build/x64/vc11/staticlib'],
		          'libraries':[
								'-lopencv_core244.lib',
								'-lopencv_imgproc244.lib',
								'-lopencv_calib3d244.lib',
								'-lopencv_features2d244.lib',
								'-lopencv_objdetect244.lib',
								'-lopencv_video244.lib',
								'-lopencv_highgui244.lib',
								'-lopencv_contrib244.lib',
								'-lopencv_flann244.lib',
								'-lopencv_ml244.lib',
								'-lopencv_gpu244.lib',
								'-lopencv_legacy244.lib',
								'-lIlmImf.lib',
								'-lzlib.lib',
								'-llibjasper.lib',
								'-llibjpeg.lib',
								'-llibpng.lib',
								'-llibtiff.lib',
								'-lcomctl32.lib',
								'-lvfw32.lib'
		          ],

					    'msvs_settings': 
					    {
			          'VCCLCompilerTool': {
			            'RuntimeLibrary': 0, # static release
			            'Optimization': 3, # /Ox, full optimization
			            'FavorSizeOrSpeed': 1, # /Ot, favour speed over size
			            'InlineFunctionExpansion': 2, # /Ob2, inline anything eligible
			            'WholeProgramOptimization': 'true', # /GL, whole program optimization, needed for LTCG
			            'OmitFramePointers': 'true',
			            'EnableFunctionLevelLinking': 'true',
			            'EnableIntrinsicFunctions': 'true',
			            'RuntimeTypeInfo': 'false',
			            'ExceptionHandling': '0',
			            'AdditionalOptions': [
			              '/MP /EHsc', '/MT'
			            ],
			          },
			          'VCLibrarianTool': {
			            'AdditionalOptions': [
			              '/LTCG', # link time code generation
			            ],
			          },
			          'VCLinkerTool': {
			            'LinkTimeCodeGeneration': 1, # link-time code generation
			            'OptimizeReferences': 2, # /OPT:REF
			            'EnableCOMDATFolding': 2, # /OPT:ICF
			            'LinkIncremental': 1, # disable incremental linking
			          	'AdditionalLibraryDirectories': ['$(OPENCV_ROOT)/build/x64/vc11/staticlib'],
			          }
			        }
		        }
		      ]
      ]
	}]
}
