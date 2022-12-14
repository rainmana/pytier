"""
    ZeroTier Central API

    ZeroTier Central Network Management Portal API.<p>All API requests must have an API token header specified in the <code>Authorization: token xxxxx</code> format.  You can generate your API key by logging into <a href=\"https://my.zerotier.com\">ZeroTier Central</a> and creating a token on the Account page.</p><p>eg. <code>curl -X GET -H \"Authorization: token xxxxx\" https://api.zerotier.com/api/v1/network</code></p><p><h3>Rate Limiting</h3></p><p>The ZeroTier Central API implements rate limiting.  Paid users are limited to 100 requests per second.  Free users are limited to 20 requests per second.</p> <p> You can get the OpenAPI spec here as well: <code>https://docs.zerotier.com/openapi/centralv1.json</code></p>  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="ZeroTier Central API",
    author="ZeroTier Support Discussion Forum",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "ZeroTier Central API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    ZeroTier Central Network Management Portal API.&lt;p&gt;All API requests must have an API token header specified in the &lt;code&gt;Authorization: token xxxxx&lt;/code&gt; format.  You can generate your API key by logging into &lt;a href&#x3D;\&quot;https://my.zerotier.com\&quot;&gt;ZeroTier Central&lt;/a&gt; and creating a token on the Account page.&lt;/p&gt;&lt;p&gt;eg. &lt;code&gt;curl -X GET -H \&quot;Authorization: token xxxxx\&quot; https://api.zerotier.com/api/v1/network&lt;/code&gt;&lt;/p&gt;&lt;p&gt;&lt;h3&gt;Rate Limiting&lt;/h3&gt;&lt;/p&gt;&lt;p&gt;The ZeroTier Central API implements rate limiting.  Paid users are limited to 100 requests per second.  Free users are limited to 20 requests per second.&lt;/p&gt; &lt;p&gt; You can get the OpenAPI spec here as well: &lt;code&gt;https://docs.zerotier.com/openapi/centralv1.json&lt;/code&gt;&lt;/p&gt;  # Authentication  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # noqa: E501
    """
)
