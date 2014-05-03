from org.lwjgl.opengl import GL11, GL12, GL13, GL21, GL30, GL31, GL33, GL42

attachment_points = {name : GL30.__dict__[name].field.getInt(None) for name in 
                     ['GL_DEPTH_ATTACHMENT', 'GL_STENCIL_ATTACHMENT', 'GL_DEPTH_STENCIL_ATTACHMENT']
                     + ['GL_COLOR_ATTACHMENT%d' % i 
                       for i in range(min(16, GL11.glGetInteger(GL30.GL_MAX_COLOR_ATTACHMENTS)))]
                     }

tex_targets = {name : globals()['GL%d' % version].__dict__[name].field.getInt(None)  
               for version, names in {
                                     11 : ['GL_TEXTURE_2D', 'GL_PROXY_TEXTURE_2D'],
                                     13 : ['GL_TEXTURE_CUBE_MAP_POSITIVE_X',
                                           'GL_TEXTURE_CUBE_MAP_NEGATIVE_X',
                                           'GL_TEXTURE_CUBE_MAP_POSITIVE_Y',
                                           'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y',
                                           'GL_TEXTURE_CUBE_MAP_POSITIVE_Z',
                                           'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z',
                                           'GL_PROXY_TEXTURE_CUBE_MAP'],
                                     30 : ['GL_TEXTURE_1D_ARRAY', 'GL_PROXY_TEXTURE_1D_ARRAY', ],
                                     31 : ['GL_TEXTURE_RECTANGLE', 'GL_PROXY_TEXTURE_RECTANGLE', ]
                                     }.items() for name in names}

internal_formats = {name : globals()['GL%d' % version].__dict__[name].field.getInt(None)  
               for version, names in {
                                     11 : ['GL_DEPTH_COMPONENT',
                                           'GL_RED', 'GL_RGB', 'GL_RGBA',
                                           'GL_R3_G3_B2',
                                            'GL_RGB4',
                                            'GL_RGB5',
                                            'GL_RGB8',
                                            'GL_RGB10',
                                            'GL_RGB12',
                                            'GL_RGBA2',
                                            'GL_RGBA4',
                                            'GL_RGB5_A1',
                                            'GL_RGBA8',
                                            'GL_RGB10_A2',
                                            'GL_RGBA12',
                                            'GL_RGBA16',
                                            ],
                                      13 : ['GL_COMPRESSED_RGB',
                                            'GL_COMPRESSED_RGBA',
                                            ],
                                     21 : ['GL_SRGB8',
                                            'GL_SRGB8_ALPHA8',
                                            'GL_COMPRESSED_SRGB',
                                            'GL_COMPRESSED_SRGB_ALPHA',
                                            ],
                                     30 : ['GL_DEPTH_STENCIL',
                                           'GL_RG',
                                           'GL_R8',
                                            'GL_R16',
                                            'GL_RG8',
                                            'GL_RG16',
                                            'GL_R16F',
                                            'GL_RG16F',
                                            'GL_RGB16F',
                                            'GL_RGBA16F',
                                            'GL_R32F',
                                            'GL_RG32F',
                                            'GL_RGB32F',
                                            'GL_RGBA32F',
                                            'GL_R11F_G11F_B10F',
                                            'GL_RGB9_E5',
                                            'GL_R8I',
                                            'GL_R8UI',
                                            'GL_R16I',
                                            'GL_R16UI',
                                            'GL_R32I',
                                            'GL_R32UI',
                                            'GL_RG8I',
                                            'GL_RG8UI',
                                            'GL_RG16I',
                                            'GL_RG16UI',
                                            'GL_RG32I',
                                            'GL_RG32UI',
                                            'GL_RGB8I',
                                            'GL_RGB8UI',
                                            'GL_RGB16I',
                                            'GL_RGB16UI',
                                            'GL_RGB32I',
                                            'GL_RGB32UI',
                                            'GL_RGBA8I',
                                            'GL_RGBA8UI',
                                            'GL_RGBA16I',
                                            'GL_RGBA16UI',
                                            'GL_RGBA32I',
                                            'GL_RGBA32UI',
                                            'GL_COMPRESSED_RED',
                                            'GL_COMPRESSED_RG',
                                            'GL_COMPRESSED_RED_RGTC1',
                                            'GL_COMPRESSED_SIGNED_RED_RGTC1',
                                            'GL_COMPRESSED_RG_RGTC2',
                                            'GL_COMPRESSED_SIGNED_RG_RGTC2',
                                             ],
                                      31 : ['GL_R8_SNORM',
                                            'GL_R16_SNORM',
                                            'GL_RG8_SNORM',
                                            'GL_RG16_SNORM',
                                            'GL_RGB8_SNORM',
                                            'GL_RGB16_SNORM',
                                            'GL_RGBA8_SNORM',
                                            ],
                                      33 : ['GL_RGB10_A2UI',
                                            ],
                                      42 : ['GL_COMPRESSED_RGBA_BPTC_UNORM',
                                            'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM',
                                            'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT',
                                            'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT',]
                                     }.items() for name in names}

formats = {name : globals()['GL%d' % version].__dict__[name].field.getInt(None)  
               for version, names in {
                                     11 : ['GL_RED', 'GL_RGB',
                                           'GL_RGBA',
                                           'GL_STENCIL_INDEX', 
                                           'GL_DEPTH_COMPONENT', 
                                           
                                           ],
                                      12 : ['GL_BGR', 'GL_BGRA', ],
                                      30 : ['GL_RG', 'GL_RED_INTEGER', 
                                           'GL_RG_INTEGER', 'GL_RGB_INTEGER', 
                                           'GL_BGR_INTEGER', 'GL_RGBA_INTEGER', 
                                           'GL_BGRA_INTEGER', 
                                            'GL_DEPTH_STENCIL'
                                            ],
                                      }.items() for name in names}

types = {name : globals()['GL%d' % version].__dict__[name].field.getInt(None)  
               for version, names in {
                                     11 : ['GL_UNSIGNED_BYTE', 'GL_BYTE', 'GL_UNSIGNED_SHORT', 'GL_SHORT', 
                                           'GL_UNSIGNED_INT', 'GL_INT', 'GL_FLOAT',
                                            ],
                                      12 : ['GL_UNSIGNED_BYTE_3_3_2', 
                                           'GL_UNSIGNED_BYTE_2_3_3_REV', 'GL_UNSIGNED_SHORT_5_6_5', 
                                           'GL_UNSIGNED_SHORT_5_6_5_REV', 'GL_UNSIGNED_SHORT_4_4_4_4', 
                                           'GL_UNSIGNED_SHORT_4_4_4_4_REV', 'GL_UNSIGNED_SHORT_5_5_5_1', 
                                           'GL_UNSIGNED_SHORT_1_5_5_5_REV', 'GL_UNSIGNED_INT_8_8_8_8', 
                                           'GL_UNSIGNED_INT_8_8_8_8_REV', 'GL_UNSIGNED_INT_10_10_10_2', 
                                           'GL_UNSIGNED_INT_2_10_10_10_REV'],
                                      }.items() for name in names}